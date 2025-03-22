import json

import pandas as pd
import logging

logger_saver = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_saver.addHandler(file_handler)
logger_saver.setLevel(logging.INFO)


class Saver:
    """Класс сохранения списка вакансий в файл .json
    или выгрузки из файла .json и преобразования в список

    Args:
        file_worker (str): путь к файлу
    Returns:
        str: сообщение об успешном
        или неуспешном выполнении задачи
    """
    file_worker: str

    def __init__(self, file_worker):
        self.file_worker = file_worker

    def save_vacancy(self, vacancies: list, path_to_file: str = "") -> str:
        """Метод сохранения списка вакансий в формате json
        в файл, путь к которому можно указать.
        Если путь не будет указан, то будет использован
        путь по умолчанию

        Args:
            vacancies (list): список вакансий
            path_to_file (str): путь к файлу.

        Returns:
            str: сообщение об успешном
            или неуспешном выполнении задачи
        """
        if path_to_file == "":
            path_to_file = self.file_worker
        try:
            with open(path_to_file, "w", encoding="utf-8") as file:
                file.write(
                    json.dumps(vacancies, indent=4, ensure_ascii=False).replace("\xa0", " ").replace("\u200b", "")
                )
                logger_saver.info(f"Write vacancies to file: {self.file_worker}")
                return "Write vacancies OK"
        
        except FileNotFoundError as error:
            logger_saver.info(error)
            return "Error, file not found"

    def load_vacancy(self, path_to_file: str = "") -> str:
        """Метод чтения списка вакансий из файла .json, путь
        к которому можно указать.
        Если путь не будет указан, то будет использован
        путь по умолчанию

        Args:
            path_to_file (str): путь к файлу.

        Returns:
            Список из файла или строка о неуспешном 
            выполнении задачи
        """
        if path_to_file == "":
            path_to_file = self.file_worker
        try:
            with open(path_to_file, "r", encoding="utf-8") as file:
                logger_saver.info(f"Ride vacancies OK, file: {path_to_file}")
                return json.load(file)
        
        except FileNotFoundError as error:
            logger_saver.info(error)
            return "Error, file not found"
