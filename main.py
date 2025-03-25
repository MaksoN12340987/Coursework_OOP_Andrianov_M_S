import logging

from src.filtering_vacancies import FilteringVacancies
from src.vacancies import VacanciOperator
from src.get_api_hh import HH
from src.saver import VacanciSaver

logger_main = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_main.addHandler(file_handler)
logger_main.setLevel(logging.INFO)


def main():
    logger_main.info("Get started main")

    # item_hh = HH("https://api.hh.ru/vacancies", "Python")
    # vacancies_hh = item_hh.load_vacancies
    item_hh = VacanciSaver("data/vacancies_hh.json")
    vacancies_hh = item_hh.load_vacancy()


    selected_vacanci = FilteringVacancies(vacancies_hh)
    print(selected_vacanci)
    selected_sort_vacanci = selected_vacanci.sorting_vacancies_for_salary("зарплата")
    print(selected_vacanci)


    save_object = VacanciSaver("data/selected_vacancies_hh.json")
    save_object.save_vacancy(selected_sort_vacanci)

    # vacancies = save_object.load_vacancy()
    # print(vacancies[0]["name"])

    logger_main.info("End main")


if __name__ == "__main__":
    main()
