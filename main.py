import logging
import re

from src.get_api_hh import HH
from src.saver import VacanciSaver
from src.vacancies import VacanciOperator

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
    save_to_file = "data/vacancies.json"

    pattern = re.compile(r"[.,?]")

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
                print(f"\nУспешно получили список вакансий, сохраню их:\n{save_to_file}")
                vacancies = VacanciSaver(vacancies_hh, save_to_file)
                print(vacancies)

                to_sort = re.sub(
                    pattern,
                    "",
                    (
                        input(
                            """Если желаете отсортировать по убываню или по возврастанию, то
                введите соответствующее слово или нажмите продолжть:\n"""
                        )
                    ),
                ).lower()
                logger_main.info(f"{to_sort}")

                filtration_ondition = re.sub(
                    pattern,
                    "",
                    (
                        input(
                            """             Если желаете отфильтровать по типу занятости, то
                введите параметр в точности:
                - Частичная занятость
                - Проектная работа
                - Полная занятость
                - Вахта
                - Гибрид
                - Удалённо
                - Разъездной
                - На месте работодателя
                или нажмите продолжть:\n"""
                        )
                    ),
                )
                logger_main.info(f"{filtration_ondition}")

                vacanci_manager = VacanciOperator({})
                sorted_vacanci = []

                selector = True
                parameter = ""

                if filtration_ondition in ["Полная занятость", "Частичная занятость", "Проектная работа", "Вахта"]:
                    parameter = "employment"

                elif filtration_ondition in ["Гибрид", "Удалённо", "Разъездной", "На месте работодателя"]:
                    parameter = "work_format"

                elif to_sort == "возврастанию":
                    selector = False
                    logger_main.info("возврастанию")

                sorted_vacanci = vacanci_manager.sorting_vacancies_for_salary(
                    vacancies_hh, selector, parameter, filtration_ondition
                )

                result_sorted = VacanciSaver(sorted_vacanci, save_to_file)
                print(result_sorted)

                if input("Если хотите сравнить вакансии по зарплате, введите 'да':\n").lower() == "да":
                    try:
                        user_select_1 = int(
                            input("Введите порядковый номер первой вакансии, которую хотите сравнить:\n").lower()
                        )
                        user_select_2 = int(
                            input("Введите порядковый номер второй вакансии, которую хотите сравнить:\n").lower()
                        )

                        vacanci_select_1 = VacanciOperator(sorted_vacanci[user_select_1 - 1])
                        vacanci_select_2 = VacanciOperator(sorted_vacanci[user_select_2 - 1])
                        if vacanci_select_1 == vacanci_select_2:
                            print("Зарплаты равны")
                        elif vacanci_select_1 < vacanci_select_2:
                            print(f"Зарплата у {user_select_2.vacncy_salary} больше")
                        elif vacanci_select_1 > vacanci_select_2:
                            print(f"Зарплата у {vacanci_select_1.vacancy_salary} больше")
                        else:
                            print("Хм, не смогли сравнить вакансии\n")
                    except Exception as error:
                        print(f"Хм, не смогли сравнить вакансии {error}\n")

                print("Если хоите сохранить все вакансии, то просто нажмите 'продолжить'")
                what_to_save = list(
                    input("Если хотите сохранить вакансии, введите порядковые номера через запятую:\n")
                    .lower()
                    .split(",")
                )
                save = []
                if what_to_save == [""]:
                    for i in range(len(sorted_vacanci)):
                        temp = VacanciOperator(sorted_vacanci[i])
                        save.append(temp())
                else:
                    for i, value in enumerate(what_to_save):
                        temp = VacanciOperator(sorted_vacanci[int(value) - 1])
                        save.append(temp())

                result = VacanciSaver(save, save_to_file)
                result.save_to_json()
                print(result)

            print("\nВозвращаюсь в главное меню\n")

        elif user_choice == "2":
            print("До следующей встречи)")
            triger = False
        else:
            print("Хм, кажется такого варианта у меня пока нет(")

    logger_main.info("End main")


if __name__ == "__main__":
    main()
