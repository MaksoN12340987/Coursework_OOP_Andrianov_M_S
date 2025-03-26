import logging
import re

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
    triger = True

    # Входные данные
    api_src = "https://api.hh.ru/vacancies"
    # Куда сохранить список вакансий, полученных из апи
    save_to_file = "data/vacancies_hh.json"
    # Куда сохранить список отсортированных и отфильтрованных вакансий
    save_to_file_sort = "data/selected_vacancies_hh.json"

    pattern = re.compile(r"\W")

    while triger:

        user_choice = re.sub(
            pattern,
            "",
            (
                input(
                    "Привет! Добро пожаловать в программу подбора вакансий\n"
                    + """Выберите необходимый пункт меню:
    1. Запросить список вакансий по ключевому слову
    2. Выйти

    Введите номер варианта: """
                )
            ),
        ).lower()

        if user_choice == "1":
            find_word = re.sub(pattern, "", input("Введите слово, по которому я подберу вакансии: ")).lower()
            item_hh = HH(api_src, find_word)
            vacancies_hh = item_hh.load_vacancies

            if vacancies_hh != []:
                print(f"\nУспешно получили список вакансий, сохраню их:\n{save_to_file}\n")
                vacancies = VacanciSaver("data/vacancies_hh.json")
                
                to_sort = re.sub(pattern, "", (
                    input(
                        """Если желаете отсортировать по убываню или по возврастанию, то
                введите соответствующее слово или нажмите продолжть:\n"""
                    ))
                ).lower()
                
                to_filtring = re.sub(pattern, "", (
                    input(
                        """Если желаете отфильтровать по убываню или по возврастанию, то
                введите соответствующее слово или нажмите продолжть:\n"""
                    ))
                ).lower()
                
                sorted_vacanci = []

                if to_sort == "убываню":
                    to_sorted_vacanci = VacanciOperator(vacancies.load_vacancy())
                    sorted_vacanci = to_sorted_vacanci.sorting_vacancies_for_salary(True)
                elif to_sort == "убываню":
                    to_sorted_vacanci = VacanciOperator(vacancies.load_vacancy())
                    sorted_vacanci = to_sorted_vacanci.sorting_vacancies_for_salary(True)
                else:
                    to_sorted_vacanci = FilteringVacancies(vacancies.load_vacancy())
                    sorted_vacanci = to_sorted_vacanci.sorting_vacancies_for_salary(False)

        elif user_choice == "2":
            print("До следующей встречи)")
            triger = False
        else:
            print("Хм, кажется такого варианта у меня пока нет(")

    # item_hh = HH("https://api.hh.ru/vacancies", "Python")
    # vacancies_hh = item_hh.load_vacancies
    # item_hh = VacanciSaver("data/vacancies_hh.json")
    # vacancies_hh = item_hh.load_vacancy()

    # selected_vacanci = FilteringVacancies(vacancies_hh)
    # print(selected_vacanci)
    # selected_sort_vacanci = selected_vacanci.sorting_vacancies_for_salary("зарплата")
    # print(selected_vacanci)

    # save_object = VacanciSaver("data/selected_vacancies_hh.json")
    # save_object.save_vacancy(selected_sort_vacanci)

    # vacancies = save_object.load_vacancy()
    # print(vacancies[0]["name"])

    logger_main.info("End main")


if __name__ == "__main__":
    main()
