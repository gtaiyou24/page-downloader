import time
from typing import Optional

from domain.model.cookie import Cookies
from domain.model.device import Device
from domain.model.page import Page, HttpStatus
from domain.model.page.html import HTML, CharacterCode
from domain.model.url import URL
from port.adapter.service.page.adapter import PageAdapter


class PageAdapterStub(PageAdapter):
    def download(self, url: URL, device: Device, cookies: Optional[Cookies], wait: Optional[int]) -> Page:
        if wait:
            time.sleep(wait)
        return Page(url, HttpStatus.OK, HTML('<!DOCTYPE><html><body></body></html>', CharacterCode.UTF_8))
