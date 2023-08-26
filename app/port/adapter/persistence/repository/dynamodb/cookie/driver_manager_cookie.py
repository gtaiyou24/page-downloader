import hashlib
from typing import Optional, NoReturn

from injector import inject

from domain.model.cookie import Cookies, Domain, Cookie, Path
from domain.model.organization.id import OrganizationId
from port.adapter.persistence.repository.dynamodb.cookie.driver import CookiesTableRow


class DriverManagerCookie:
    @inject
    def __init__(self):
        if not CookiesTableRow.exists():
            CookiesTableRow.create_table()

    def find_cookies_by_organization_id_and_domains(self, organization_id: OrganizationId, domains: set[Domain]) -> Optional[Cookies]:
        cookies = set()
        for domain in domains:
            cookie_table_row = CookiesTableRow.get(self.__id(organization_id, domain))
            contents = eval(cookie_table_row.contents)
            cookies.add(Cookie(domain, Path(contents['path']), contents['name'], contents['value']))

        return Cookies(organization_id, cookies)

    def save(self, cookies) -> NoReturn:
        pass

    def delete(self, organization_id: OrganizationId) -> NoReturn:
        pass

    @staticmethod
    def __id(organization_id: OrganizationId, domain: Domain) -> str:
        return hashlib.sha256(f'{organization_id.value}_{domain.value}').hexdigest()
