import time
from typing import Optional, NoReturn

import requests
from selenium.common import JavascriptException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from domain.model.cookie import Cookies
from domain.model.device import Device
from domain.model.page import Page, HttpStatus
from domain.model.page.html import CharacterCode, HTML
from domain.model.url import URL
from exception import SystemException, ErrorCode
from port.adapter.service.page.adapter import PageAdapter
from port.adapter.service.page.adapter.selenium import ChromeBuilder


class SeleniumAdapter(PageAdapter):
    def __init__(self, wait: int = 10):
        self.__builder = ChromeBuilder()
        self.__wait = wait

    def download(self, url: URL, device: Device, cookies: Optional[Cookies], wait: Optional[int]) -> Page:
        web_driver = self.__builder.device(device).build()

        if cookies:
            for cookie in cookies.cookie_set:
                web_driver.add_cookie({
                    'name': cookie.name, 'value': cookie.value, 'domain': cookie.domain, 'path': cookie.path})

        try:
            web_driver.implicitly_wait(wait if wait else 30)
            web_driver.get(url.value)
        except TimeoutException:
            raise SystemException(ErrorCode.PAGE_TIMEOUT, 'page {} timeout.'.format(url.value))

        # 最下部までスクロールする
        self.__scroll_to_bottom(web_driver)

        # ページの読み込みが完了するまで待機する
        WebDriverWait(web_driver, self.__wait)\
            .until(expected_conditions.presence_of_all_elements_located)

        if wait:
            time.sleep(wait)

        url = URL(web_driver.current_url)
        response = requests.get(
            url.value,
            headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) '
                                   'AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone9'
                                   ',1;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]'}
        )
        html = HTML(web_driver.page_source, CharacterCode.value_of(response.apparent_encoding))

        web_driver.quit()

        return Page(url, HttpStatus.value_of(response.status_code), html)

    @staticmethod
    def __scroll_to_bottom(web_driver) -> NoReturn:
        try:
            web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except JavascriptException as e:
            # NOTE: 上記の方法でスクロールできない場合
            web_driver.find_element(By.TAG_NAME, "body").click()
            web_driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
