from typing import NoReturn, Set

from injector import inject

from domain.model.cookie import CookieRepository, Cookies, Domain
from domain.model.organization.id import OrganizationId
from port.adapter.persistence.repository.dynamodb.cookie import CacheLayerCookie, DriverManagerCookie


class DynamoCookieRepository(CookieRepository):
    @inject
    def __init__(self, cache_layer_cookie: CacheLayerCookie, driver_manager_cookie: DriverManagerCookie):
        self.__cache_layer_cookie = cache_layer_cookie
        self.__driver_manager_cookie = driver_manager_cookie

    def cookies_of(self, organization_id: OrganizationId, domains: Set[Domain]) -> Cookies:
        return self.__cache_layer_cookie.cookies_or_origin(organization_id, domains)

    def save(self, cookies: Cookies) -> NoReturn:
        self.__driver_manager_cookie.save(cookies)

    def delete(self, organization_id: OrganizationId) -> NoReturn:
        self.__driver_manager_cookie.delete(organization_id)
