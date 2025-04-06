import logging

import requests

from src.abstract_clases import Parser

logger_hh = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_hh.addHandler(file_handler)
logger_hh.setLevel(logging.INFO)


class HH(Parser):
    """Класс для получения списка вакансий
    из с API HeadHunter

    Args:
        url (str): адрес апи
        keyword (str): ключевое слово для подбора вакансий

    Returns:
        list: список вакансий
    """

    url: str
    keyword: str

    def __init__(self, url, keyword):
        self.__url = url
        self.__vacancies = []
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": keyword, "page": 1, "per_page": 1}

    def __str__(self):
        """Метод срабатывает при print(object_hh)
        Выводит строку с ссылкой на апи, заголовком и параметрами
        """
        return f"{self.__url}, {self.__headers}, {self.__params}"

    @property
    def load_vacancies(self):
        """Метод получает список вакансий из апи hh.ru

        Args:
            keyword (str): ключевое слово для подбора
            вакансий

        Raises:
            ValueError: ошибка, вызываемая при не корректном
            адресе апи

        Returns:
            list: список вакансий, найденых по ключевому слову
        """
        while self.__params.get("page") != 20:
            vacancies = []
            try:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                if response.status_code == 200:
                    try:
                        vacancies.append(response.json()["items"][0])
                    except IndexError:
                        logger_hh.warning(f"sent an empty list(:\n{response.json()["items"]}")

            except requests.exceptions.ConnectionError:
                vacancies = []
                raise ConnectionError("Connection Error. Please check your network connection.")

            except requests.exceptions.HTTPError:
                vacancies = []
                raise ValueError("HTTP Error. Please check the URL.")

            finally:
                logger_hh.debug(f"Attempt to access API completed, returned:\n{vacancies[:50]}")

            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1
        return self.__vacancies
