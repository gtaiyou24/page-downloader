from typing import Optional

from injector import singleton, inject

from application.page.dpo import DownloadedPageDpo
from domain.model.device.device import Device
from domain.model.page import PageService
from domain.model.url import URL


@singleton
class PageApplicationService:
    @inject
    def __init__(self, page_service: PageService):
        self.__page_service = page_service

    def download(self, an_url: str, a_device: str, an_organization_id: Optional[str], wait: Optional[int]) -> DownloadedPageDpo:
        url = URL(an_url)

        cookies = None
        # if an_organization_id:
        #     organization_id = OrganizationId(an_organization_id)
        #     cookies = self.__cookie_repository.cookies_of(organization_id, Domain.domains_of(url))

        device = Device.value_of(a_device)
        page = self.__page_service.download(url, device, cookies, wait)

        return DownloadedPageDpo(page)
