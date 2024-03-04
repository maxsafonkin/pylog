import logging

from .constants import LogLevel
from .environ import FILE_PATH

class PyLog:
    _MSG_FORMAT = "[ %(asctime)s ] [ %(levelname)s ] %(message)s"
    _DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

    def __init__(self, file_path: str | None) -> None:
        self._logger = logging.getLogger(__name__)
        
        self._log_level = LogLevel.DEBUG
        self._logger.setLevel(self._log_level)

        self._formatter = logging.Formatter(fmt=self._MSG_FORMAT, datefmt=self._DATE_FORMAT)
        self._set_format()

        if file_path is not None:
            self._set_file_output(file_path)

    def set_level(self, log_level: LogLevel) -> None:
        self._log_level = log_level
        self._logger.setLevel(self._log_level)

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

    def _set_format(self) -> None:
        formatter_handler = logging.StreamHandler()
        formatter_handler.setLevel(self._log_level)
        formatter_handler.setFormatter(self._formatter)

        self._logger.addHandler(formatter_handler)

    def _set_file_output(self, path: str) -> None:
        file_handler = logging.FileHandler(path)
        file_handler.setLevel(self._log_level)
        file_handler.setFormatter(self._formatter)

        self._logger.addHandler(file_handler)


pylog = PyLog(FILE_PATH)

