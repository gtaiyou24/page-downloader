import abc
from typing import Optional

from domain.model.cookie import Cookies
from domain.model.device import Device
from domain.model.page import Page
from domain.model.url import URL


class PageAdapter(abc.ABC):
    @abc.abstractmethod
    def download(self, url: URL, device: Device, cookies: Optional[Cookies], wait: Optional[int]) -> Page:
        pass
