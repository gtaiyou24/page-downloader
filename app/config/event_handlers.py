from typing import NoReturn

from di import DIContainer, DI
from domain.model.cookie import CookieRepository
from domain.model.page import PageService
from port.adapter.service.page import PageServiceImpl
from port.adapter.service.page.adapter import PageAdapter
from port.adapter.service.page.adapter.selenium import SeleniumAdapter
from port.adapter.standalone.adapterstub import PageAdapterStub
from port.adapter.standalone.inmemory import InMemCookieRepository


def startup_handler() -> NoReturn:
    for di in [DI.of(PageService, {}, PageServiceImpl),
               DI.of(PageAdapter, {'Stub': PageAdapterStub}, SeleniumAdapter),
               DI.of(CookieRepository, {}, InMemCookieRepository)]:
        DIContainer.instance().register(di)


def shutdown_handler() -> NoReturn:
    pass
