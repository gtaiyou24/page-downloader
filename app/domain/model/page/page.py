from dataclasses import dataclass

from domain.model.page import HttpStatus
from domain.model.page.html import HTML
from domain.model.url import URL


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Page:
    url: URL
    http_status: HttpStatus
    html: HTML

    def __init__(self, url: URL, http_status: HttpStatus, html: HTML):
        assert url, "URLは必須です"
        assert http_status, "HTTPステータスは必須です"
        assert html, "HTMLは必須です"
        super().__setattr__("url", url)
        super().__setattr__("http_status", http_status)
        super().__setattr__("html", html)

    def is_ok(self) -> bool:
        return self.http_status.is_200() and self.html.is_not_empty()
