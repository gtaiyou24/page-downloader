from di import DIContainer
from fastapi import APIRouter

from application.cookie.command import SaveCookiesCommand
from application.cookie.service import CookieApplicationService
from port.adapter.resource.cookie.request import RequestSaveCookies

router = APIRouter(
    prefix='/cookies',
    tags=['クッキー系']
)


@router.post('/', name='クッキー保存機能')
def save(request: RequestSaveCookies):
    cookie_application_service: CookieApplicationService = DIContainer.instance().resolve(CookieApplicationService)

    command = SaveCookiesCommand(
        organization_id=request.organization_id,
        cookies={SaveCookiesCommand.Cookie(
            domain=cookie.domain, path=cookie.path, name=cookie.name, value=cookie.value) for cookie in request.cookies}
    )
    cookie_application_service.save(command)


@router.delete('/', name='クッキー削除機能')
def delete(organization_id: str):
    cookie_application_service: CookieApplicationService = DIContainer.instance().resolve(CookieApplicationService)
    cookie_application_service.delete(organization_id)
