import requests as re

from src.abstract_clases import Parser
import logging

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
    Returns:
        list: список вакансий
    """
    url: str

    def __init__(self, url):
        self.__url = url
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 1, "per_page": 1}
        self.vacancies = []
        super().__init__()

    def load_vacancies(self, keyword: str = ""):
        """_summary_

        Args:
            keyword (str): ключевое слово для подбора
            вакансий

        Raises:
            ValueError: ошибка, вызываемая при не корректном
            адресе апи

        Returns:
            list: список вакансий, найденых по ключевому слову
        """
        self.params["text"] = keyword

        while self.params.get("page") != 3:
            try:
                response = re.get(self.__url, headers=self.headers, params=self.params)
            
            except re.exceptions.ConnectionError:
                print("Connection Error. Please check your network connection.")
                response = []
            
            except re.exceptions.HTTPError:
                raise ValueError("HTTP Error. Please check the URL.")
            
            finally:
                logger_hh.info(f"Status code:\n{response}")

            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
        return self.vacancies
