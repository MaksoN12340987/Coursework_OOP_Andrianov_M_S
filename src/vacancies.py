from src.abstract_clases import Vacanci
import re

import logging


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

    pull_vacanci: list

    def __init__(self, pull_vacanci):
        if pull_vacanci != []:
            self.job_title = pull_vacanci[0]["name"]
            self.vacancy_link = pull_vacanci[0]["alternate_url"]
            try:
                self.salary = f"{pull_vacanci[0]["salary"]["from"]}"
            except TypeError:
                self.salary = "Не указана"

            pattern = re.compile(r"<\D.\w+>")
            self.job_requirements = re.sub(pattern, "", f"{pull_vacanci[0]["snippet"]["requirement"]}\n")
        else:
            self.job_title = ""
            self.vacancy_link = ""
            self.salary = 0
            self.job_requirements = "\n"
        self.number_of_vacancies = len(pull_vacanci)
        self.__pull_vacanci = pull_vacanci
        super().__init__()

    def __str__(self) -> str:
        super().__str__()
        result = "\nСписок вакансий:\n"
        for i, value in enumerate(self.__pull_vacanci):
            try:
                result += f"{i + 1}. {value["name"]} {value["salary"]["from"]}\n"
            except TypeError:
                result += f"{i + 1}. {value["name"]} {value["salary"]}\n"

        if len(self.__pull_vacanci) < 1:
            result += "Упс, вакансий не нашлось(\n"

        return result

    def __call__(self):
        return self.__pull_vacanci

    def vacancy_job_title(self, number_vacanci: int) -> str:
        """Метод возвращает название вакансии по её порядковому номеру
        Args:
            number_vacanci (int): _description_

        Returns:
            str: _description_
        """
        super().vacancy_job_title()
        if number_vacanci < self.number_of_vacancies + 1:
            return f"{self.__pull_vacanci[number_vacanci - 1]["name"]}"
        else:
            return "Упс, вакансий не нашлось(\n"

    def vacancy_link_to_vacancy(self, number_vacanci: int) -> str:
        """Метод возвращает ссылку на вакансию по её порядковому номер

        Args:
            number_vacanci (int): порядковый номер вакансии

        Returns:
            str: ссылка на вакансию
        """
        super().vacancy_link_to_vacancy()
        if number_vacanci < self.number_of_vacancies + 1:
            return f"{self.__pull_vacanci[number_vacanci - 1]["alternate_url"]}"
        else:
            return "Упс, вакансий не нашлось(\n"

    def vacancy_salary(self, number_vacanci: int) -> str:
        """Метод возвращает зарплату по порядковому номеру вакансии

        Args:
            number_vacanci (int): порядковый номер вакансии

        Returns:
            str: зарплата и валюта
        """
        super().vacancy_salary()
        if number_vacanci < self.number_of_vacancies + 1:
            try:
                result = f"{self.__pull_vacanci[number_vacanci - 1]["salary"]["from"]} "
                result += f"{self.__pull_vacanci[number_vacanci - 1]["salary"]["currency"]}"
                return result
            except TypeError:
                return "Не указана"
        else:
            return "Упс, вакансий не нашлось(\n"

    def vacancy_job_requirements(self, number_vacanci: int) -> str:
        """Метод возвращает требования к соискателю по порядковому номеру вакансии

        Args:
            number_vacanci (int): порядковый номер вакансии

        Returns:
            str: _description_
        """
        super().vacancy_job_requirements()
        if number_vacanci < self.number_of_vacancies + 1:
            pattern = re.compile(r"<\D.\w+>")
            return re.sub(pattern, "", f"{self.__pull_vacanci[number_vacanci - 1]["snippet"]["requirement"]}\n")
        else:
            return "Упс, вакансий не нашлось(\n"

    def sorting_vacancies_for_salary(self, selector: bool = True) -> list:
        """Метод сортирует вакансии по зарплате и возвращает список

        Args:
            selector (bool, optional): селектор направления сортировки:
            True - по умолчанию, от большей к меньшей

        Returns:
            list: отсортированный список вакансий
        """
        for i, value in enumerate(self.__pull_vacanci):
            if not value["salary"]:
                value["salary"] = {"from": 0}
        self.__pull_vacanci.sort(key=lambda operation_list: operation_list["salary"]["from"], reverse=selector)
        super().sorting_vacancies_for_salary()
        return self.__pull_vacanci
