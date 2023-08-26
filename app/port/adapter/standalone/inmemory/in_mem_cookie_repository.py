from typing import NoReturn, Optional, Set, Dict

from domain.model.cookie import CookieRepository, Cookies, Domain
from domain.model.organization.id import OrganizationId


class InMemCookieRepository(CookieRepository):
    __cookies: Dict[str, Cookies] = {}

    def cookies_of(self, organization_id: OrganizationId, domains: Set[Domain]) -> Optional[Cookies]:
        optional_cookies = self.__cookies.get(organization_id.value, None)
        if optional_cookies is None:
            return None

        cookies = set()
        for cookie in optional_cookies.cookie_set:
            if cookie.domain in domains:
                cookies.add(cookie)
        return Cookies(organization_id, cookies)

    def save(self, cookies: Cookies) -> NoReturn:
        self.__cookies[cookies.organization_id.value] = cookies

    def delete(self, organization_id: OrganizationId) -> NoReturn:
        self.__cookies.pop(organization_id.value)
