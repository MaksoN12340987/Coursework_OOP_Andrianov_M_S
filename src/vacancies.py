import logging
import re

from src.abstract_clases import Vacanci

logger_vacancies = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_vacancies.addHandler(file_handler)
logger_vacancies.setLevel(logging.INFO)


class VacanciOperator(Vacanci):
    """Класс работы с вакансиями
    vacancy_job_title - метод возвращает название вакансии по её порядковому номеру
    vacancy_link_to_vacancy - метод возвращает ссылку на вакансию по её порядковому номеру
    vacancy_salary - метод возвращает зарплату по порядковому номеру вакансии
    vacancy_job_requirements - метод возвращает требования к соискателю по порядковому номеру вакансии

    Args:
        Vacanci (_type_): список вакансий
    """

    vacanci: dict

    __slots__ = "vacanci"

    def __init__(self, vacanci):
        checked_values = self.__inpu_data_validation(vacanci)
        self.__job_id = checked_values["id"]
        self.__job_link = checked_values["link"]
        self.__job_title = checked_values["title"]
        self.__job_salary = checked_values["salary"]
        self.__job_requirements = checked_values["requirements"]

    def __inpu_data_validation(self, vacanci_dict: dict):
        if vacanci_dict != {}:
            job_id = vacanci_dict["id"]
            job_title = vacanci_dict["name"]
            vacancy_link = vacanci_dict["alternate_url"]
            try:
                salary = f"{vacanci_dict["salary"]["from"]}"
            except TypeError:
                salary = 0

            pattern = re.compile(r"<\D.\w+>")
            job_requirements = re.sub(pattern, "", f"{vacanci_dict["snippet"]["requirement"]}\n")
        else:
            job_id = 0
            job_title = ""
            vacancy_link = ""
            salary = 0
            job_requirements = ""

        return {
            "id": job_id,
            "link": vacancy_link,
            "title": job_title,
            "salary": salary,
            "requirements": job_requirements,
        }

    def __str__(self) -> str:
        return self.__job_salary

    def __call__(self):
        return {
            "id": self.__job_id,
            "link": self.__job_link,
            "name": self.__job_title,
            "salary": self.__job_salary,
            "requirements": self.__job_requirements,
        }

    @property
    def vacancy_id(self) -> str:
        """Метод возвращает зарплату по порядковому номеру вакансии

        Args:
            number_vacanci (int): порядковый номер вакансии

        Returns:
            str: зарплата и валюта
        """
        return f"id вакансии:\n{self.__job_id}"

    @property
    def vacancy_salary(self) -> str:
        """Метод возвращает зарплату по порядковому номеру вакансии

        Args:
            number_vacanci (int): порядковый номер вакансии

        Returns:
            str: зарплата и валюта
        """
        return f"Зарплата:\n{self.__job_salary}"

    @property
    def vacancy_job_title(self) -> str:
        """Метод возвращает название вакансии по её порядковому номеру
        Args:
            number_vacanci (int): номер вакансии в списке

        Returns:
            str: Строка
        """
        return f"Должность:\n{self.__job_title}"

    @property
    def vacancy_link_to_vacancy(self) -> str:
        """Метод возвращает ссылку на вакансию по её порядковому номер

        Args:
            number_vacanci (int): номер вакансии в списке

        Returns:
            str: Строка
        """
        return f"Ссылка на вакансию:\n{self.__job_link}"

    @property
    def vacancy_job_requirements(self) -> str:
        """Метод возвращает требования к соискателю по порядковому номеру вакансии

        Args:
            number_vacanci (int): порядковый номер вакансии

        Returns:
            str: Строка
        """
        return f"Требоапния к соискателю:\n{self.__job_requirements}"

    def __eq__(self, comparison_instance):
        return comparison_instance == self.__job_salary

    def __lt__(self, comparison_instance):
        return comparison_instance < self.__job_salary

    def __gt__(self, comparison_instance):
        return comparison_instance > self.__job_salary

    @staticmethod
    def sorting_vacancies_for_salary(
        pull_vacanci: list, selector: bool = True, parameter: str = "", filters: str = ""
    ) -> list:
        """Метод сортирует вакансии по зарплате и возвращает список

        Args:
            selector (bool, optional): селектор направления сортировки:
            True - по умолчанию, от большей к меньшей

        Returns:
            list: отсортированный список вакансий
        """
        result = []
        for i, value in enumerate(pull_vacanci):
            if not value["salary"]:
                value["salary"] = {"from": 0}
            elif not value["salary"]["from"]:
                value["salary"] = {"from": 0}

        pull_vacanci.sort(key=lambda operation_list: operation_list["salary"]["from"], reverse=selector)

        if parameter == "employment":
            pattern = re.compile(f"{filters}")
            logger_vacancies.info(f"Фильтрую по employment\n'{pattern}'")

            for i, value in enumerate(pull_vacanci):
                if re.search(pattern, f"{value["employment"]["name"]}"):
                    result.append(value)

        elif parameter == "work_format":
            pattern = re.compile(f"{filters}")
            logger_vacancies.info(f"Фильтрую по work_format\n'{pattern}'")

            for i, value in enumerate(pull_vacanci):
                if re.search(pattern, f"{str(value["work_format"])}"):
                    result.append(value)

        else:
            print(f"Параметр {parameter} не найден")
            logger_vacancies.warning(f"Параметр {parameter} не найден, возвращаю []")
            result = pull_vacanci
        return result
