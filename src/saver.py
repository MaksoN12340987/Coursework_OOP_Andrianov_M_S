import json
import logging

from src.abstract_clases import Saver

logger_saver = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_saver.addHandler(file_handler)
logger_saver.setLevel(logging.INFO)


class VacanciSaver(Saver):
    """Класс сохранения списка вакансий в файл .json
    или выгрузки из файла .json и преобразования в список

    Args:
        file_worker (str): путь к файлу
    Returns:
        str: сообщение об успешном
        или неуспешном выполнении задачи
    """

    file_worker: str
    pull_vacanci: list

    def __init__(self, pull_vacanci: list, file_worker: str):
        if file_worker == "":
            file_worker = "data/vacancies.json"
        self.__file_worker = file_worker
        self.__pull_vacanci = pull_vacanci

    def __str__(self) -> str:
        result = "\nСписок вакансий:\n"
        for i, value in enumerate(self.__pull_vacanci):
            try:
                result += f"{i + 1}. {value["name"]}\n"
            except TypeError:
                result += f"{i + 1}. {value["name"]}\n"

        if len(self.__pull_vacanci) < 1:
            result += "Упс, вакансий не нашлось(\n"

        return result

    def save_to_json(self, path_to_file: str = "") -> str:
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
            path_to_file = self.__file_worker
        load = ""

        try:
            load = self.load_to_json(path_to_file)
            if load:
                for i, value in enumerate(self.__pull_vacanci):
                    if value in load:
                        pass
                    else:
                        load.append(value)
                        logger_saver.info(f"Apendet: {value}")
        except json.JSONDecodeError:
            load = self.__pull_vacanci
            logger_saver.info(f"Файл пуст: {self.__file_worker}")

        try:
            with open(path_to_file, "w", encoding="utf-8") as file:
                file.write(
                    json.dumps(load, indent=4, ensure_ascii=False).replace("\xa0", " ").replace("\u200b", "") + "\n"
                )
                logger_saver.info(f"Write vacancies to file: {self.__file_worker}")
                return "Write vacancies OK"

        except PermissionError as error:
            logger_saver.info(f"{error}!!!")
            raise PermissionError("Error! Access denied or file with such name cannot be created")

    def load_to_json(self, path_to_file: str = "") -> list:
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
            path_to_file = self.__file_worker
        try:
            with open(path_to_file, "r", encoding="utf-8") as file:
                logger_saver.info(f"Ride vacancies OK, file: {path_to_file}")
                return json.load(file)

        except FileNotFoundError as error:
            logger_saver.info(error)
            print("Error, file not found")
            return []

        except PermissionError as error:
            logger_saver.info(f"{error}!!!")
            raise PermissionError("File access error")

    def cleaning_file(self, path_to_file: str = ""):
        if path_to_file == "":
            path_to_file = self.__file_worker
        try:
            with open(path_to_file, "w", encoding="utf-8") as file:
                file.write("")
            return "Clear vacancies OK"

        except PermissionError as error:
            logger_saver.info(f"{error}!!!")
            raise PermissionError("File access error")
