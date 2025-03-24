import logging

from src.vacancies import VacanciOperator
from src.get_api_hh import HH
from src.saver import Saver

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
    # print(type(vacancies_hh))

    save_object = Saver("data/vacancies_hh.json")

    # save_object.save_vacancy(vacancies_hh)
    vacancies = save_object.load_vacancy()

    pull_vacanci = VacanciOperator(vacancies)
    pull_vacanci.sorting_vacancies("")

    logger_main.info("End main")


if __name__ == "__main__":
    main()
