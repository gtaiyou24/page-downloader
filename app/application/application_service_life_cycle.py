from typing import NoReturn, Optional

from slf4py import set_logger


@set_logger
class ApplicationServiceLifeCycle:
    def begin(self, is_listening: bool = False) -> NoReturn:
        if is_listening:
            self.listen()
        # self.__session.begin()

    def fail(self, exception: Optional[Exception] = None) -> NoReturn:
        # self.__session.rollback()
        if exception is not None:
            raise exception

    def success(self) -> NoReturn:
        # self.__session.commit()
        self.log.debug('transaction is committed')

    def listen(self) -> NoReturn:
        self.log.debug('start listening')
