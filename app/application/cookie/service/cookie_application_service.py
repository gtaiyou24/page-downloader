from typing import NoReturn

from injector import singleton, inject
from slf4py import set_logger

from application import ApplicationServiceLifeCycle
from application.cookie.command import SaveCookiesCommand
from domain.model.cookie import CookieRepository, Cookies, Cookie, Domain, Path
from domain.model.organization.id import OrganizationId


@set_logger
@singleton
class CookieApplicationService:
    @inject
    def __init__(self,
                 application_service_life_cycle: ApplicationServiceLifeCycle,
                 cookie_repository: CookieRepository):
        self.__application_service_life_cycle = application_service_life_cycle
        self.__cookie_repository = cookie_repository

    def save(self, command: SaveCookiesCommand) -> NoReturn:
        cookies = Cookies(
            OrganizationId(command.organization_id),
            {Cookie(Domain(cookie.domain), Path(cookie.path), cookie.name, cookie.value) for cookie in command.cookies}
        )

        try:
            self.__application_service_life_cycle.begin(False)
            self.__cookie_repository.save(cookies)
            self.__application_service_life_cycle.success()
        except Exception as e:
            self.log.error(e)
            self.__application_service_life_cycle.fail(e)

    def delete(self, an_organization_id: str) -> NoReturn:
        try:
            self.__application_service_life_cycle.begin(False)
            self.__cookie_repository.delete(OrganizationId(an_organization_id))
            self.__application_service_life_cycle.success()
        except Exception as e:
            self.log.error(e)
            self.__application_service_life_cycle.fail(e)
