import abc
from typing import NoReturn, Optional, Set

from domain.model.cookie import Cookies, Domain
from domain.model.organization.id import OrganizationId


class CookieRepository(abc.ABC):
    @abc.abstractmethod
    def cookies_of(self, organization_id: OrganizationId, domains: Set[Domain]) -> Optional[Cookies]:
        pass

    @abc.abstractmethod
    def save(self, cookies: Cookies) -> NoReturn:
        pass

    @abc.abstractmethod
    def delete(self, organization_id: OrganizationId) -> NoReturn:
        pass
