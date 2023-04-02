from dataclasses import dataclass
from typing import Set

from domain.model.cookie import Cookie
from domain.model.organization.id import OrganizationId


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Cookies:
    organization_id: OrganizationId
    cookie_set: Set[Cookie]

    def __init__(self, organization_id: OrganizationId, cookies: Set[Cookie]):
        assert organization_id, '組織IDは必須です。'
        assert cookies, 'クッキー一覧は必須です。'
        super().__setattr__('organization_id', organization_id)
        super().__setattr__('cookie_set', cookies)
