import logging
import re

from src.vacancies import VacanciOperator


logger_filtering = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_filtering.addHandler(file_handler)
logger_filtering.setLevel(logging.INFO)


class FilteringVacancies(VacanciOperator):
    pull_vacanci: list

    def __init__(self, pull_vacanci):
        super().__init__(pull_vacanci)
        self.__pull_vacanci = pull_vacanci

    def __str__(self) -> str:
        result = "\nСписок вакансий:\n"
        for i, value in enumerate(self.__pull_vacanci):
            try:
                result += f"{i + 1}. {value["name"]} {value["salary"]["from"]}\n"
            except TypeError:
                result += f"{i + 1}. {value["name"]} {value["salary"]}\n"

        if len(self.__pull_vacanci) < 1:
            result += "Упс, вакансий не нашлось(\n"

        return result

    def sorting_vacancies_for_salary(self, triger: bool = True, parameter: str = "", filters: str = "", selector: bool = True) -> list:
        """Метод фильтрует вакансии по:
        1 "зарплата" указана\нет
        2 "тип занятости" полная или другая

        Args:
            selector (bool, optional): _description_. Defaults to True.
            filter (str, optional): _description_. Defaults to "".
            parameters (str, optional): _description_. Defaults to "".

        Returns:
            list: _description_
        """
        if triger:
            super().sorting_vacancies_for_salary(selector)
        parameter = parameter.lower()
        filters = filters.lower().title()
        result = []

        if parameter == "зарплата" or parameter == "1":
            logger_filtering.warning(f"Фильтрую по зарплате")

            for i, value in enumerate(self.__pull_vacanci):
                if value["salary"]["from"] > 0:
                    result.append(value)

        elif parameter == "тип занятости" or parameter == "2":
            logger_filtering.warning(f"Фильтрую по тип занятости")
            pattern = re.compile(f"<{filters}+>")

            for i, value in enumerate(self.__pull_vacanci):
                if re.search(pattern, f"{value["schedule"]["name"]}"):
                    result.append(value)

        else:
            print(f"Параметр {parameter} не найден")
            logger_filtering.warning(f"Параметр {parameter} не найден, возвращаю []")
            result = self.__pull_vacanci

        self.__pull_vacanci = result
        return result
