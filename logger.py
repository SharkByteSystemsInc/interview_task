from logging import (
    Formatter,
    Logger as L,
    StreamHandler,
)
from typing import Union


class Logger(L):

    def __init__(
        self,
        name: str = 'pi',
        level: Union[str, int] = 'DEBUG',
    ):
        super().__init__(name, level)
        stream_handler = StreamHandler()
        stream_handler.setFormatter(Formatter(
            fmt='{asctime}.{msecs:0<3.0f} {levelname:<5} \t{message}',
            datefmt='%Y-%m-%d %H:%M:%S',
            style='{',
        ))
        self.handlers = [stream_handler]


logger: Logger = Logger()
