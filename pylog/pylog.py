import logging

from .constants import LogLevel


class PyLog:
    _MSG_FORMAT = "[ %(asctime)s ] [ %(levelname)s ] %(message)s"
    _DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

    def __init__(self, log_level: str = LogLevel.INFO) -> None:
        self._logger = logging.getLogger(__name__)

        log_level = LogLevel(log_level)
        self._logger.setLevel(log_level)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt=self._MSG_FORMAT, datefmt=self._DATE_FORMAT)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def set_level(self, log_level: LogLevel) -> None:
        self._logger.setLevel(log_level)

    def debug(self, msg: str) -> None:
        self._logger.debug(msg)

    def info(self, msg: str) -> None:
        self._logger.info(msg)

    def warning(self, msg: str) -> None:
        self._logger.warning(msg)

    def error(self, msg: str) -> None:
        self._logger.error(msg)

    def critical(self, msg: str) -> None:
        self._logger.critical(msg)


pylog = PyLog()
