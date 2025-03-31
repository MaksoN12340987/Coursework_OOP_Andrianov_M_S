# Positive tests
def test_save_vacancy(object_vacanci_operator, return_vacancy_job_requirements):
    assert object_vacanci_operator.vacancy_job_title(1) == "Golang Developer"
    assert object_vacanci_operator.vacancy_link_to_vacancy(1) == "https://hh.ru/vacancy/118520774"
    assert object_vacanci_operator.vacancy_salary(1) == "Не указана"
    assert object_vacanci_operator.vacancy_job_requirements(1) == return_vacancy_job_requirements


def test_save_vacancy_salary(object_object_vacanci_operator_salary):
    assert object_object_vacanci_operator_salary.vacancy_salary(2) == "100000 RUR"


def test_save_vacancy_sorting(object_object_vacanci_operator_salary, sorted_vacancies):
    assert object_object_vacanci_operator_salary.sorting_vacancies_for_salary() == sorted_vacancies


def test_save_vacancy_str(object_object_vacanci_operator_salary, capsys):
    print(object_object_vacanci_operator_salary)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """
Список вакансий:
1. Golang Developer None
2. Тестировщик 100000\n
"""
    )


# Negative tests
def test_save_vacancy_list_clear(object_vacanci_operator_list_clear):
    assert object_vacanci_operator_list_clear.job_title == ""
    assert object_vacanci_operator_list_clear.vacancy_link == ""
    assert object_vacanci_operator_list_clear.salary == 0
    assert object_vacanci_operator_list_clear.job_requirements == "\n"


def test_save_vacancy_str_list_clear(object_vacanci_operator_list_clear, capsys):
    print(object_vacanci_operator_list_clear)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """
Список вакансий:
Упс, вакансий не нашлось(\n
"""
    )


def test_save_vacancy_salary_negative(object_object_vacanci_operator_salary):
    assert object_object_vacanci_operator_salary.vacancy_salary(1) == "Не указана"
    assert object_object_vacanci_operator_salary.salary == "Не указана"


def test_save_vacancy_operator_list_clear(object_vacanci_operator):
    assert object_vacanci_operator.vacancy_job_title(10) == "Упс, вакансий не нашлось(\n"
    assert object_vacanci_operator.vacancy_link_to_vacancy(10) == "Упс, вакансий не нашлось(\n"
    assert object_vacanci_operator.vacancy_salary(10) == "Упс, вакансий не нашлось(\n"
    assert object_vacanci_operator.vacancy_job_requirements(109) == "Упс, вакансий не нашлось(\n"
