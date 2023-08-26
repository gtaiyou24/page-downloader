from typing import Optional

from injector import inject

from domain.model.cookie import Cookies
from domain.model.device import Device
from domain.model.page import PageService, Page
from domain.model.url import URL
from port.adapter.service.page.adapter import PageAdapter


class PageServiceImpl(PageService):
    @inject
    def __init__(self, page_adapter: PageAdapter):
        self.__page_adapter = page_adapter

    def download(self, url: URL, device: Device, cookies: Optional[Cookies], wait: Optional[int]) -> Page:
        return self.__page_adapter.download(url, device, cookies, wait)
