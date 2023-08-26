from typing import Optional

from cachetools import TTLCache, cached
from injector import inject

from domain.model.cookie import Cookies, Domain
from domain.model.organization.id import OrganizationId
from port.adapter.persistence.repository.dynamodb.cookie import DriverManagerCookie


class CacheLayerCookie:
    """ローカルキャッシュを保持するクラス"""
    # 60秒 × 15分
    __TTL = 60 * 15

    @inject
    def __init__(self, driver_manager_cookie: DriverManagerCookie):
        self.__driver_manager_cookie = driver_manager_cookie

    @cached(cache=TTLCache(maxsize=128, ttl=__TTL))
    def cookies_or_origin(self, organization_id: OrganizationId, domains: set[Domain]) -> Optional[Cookies]:
        return self.__driver_manager_cookie.find_cookies_by_organization_id_and_domains(organization_id, domains)
