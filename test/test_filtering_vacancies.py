def test__filtering_vacancies_full(object_filtering_vacancies_defolt):
    object_of_comparison = object_filtering_vacancies_defolt.sorting_vacancies_for_salary(
        False, "employment", "Полная занятость"
    )
    assert object_of_comparison[0]["employment"]["name"] == "Полная занятость"


def test__filtering_vacancies_part(object_filtering_vacancies_defolt):
    object_of_comparison = object_filtering_vacancies_defolt.sorting_vacancies_for_salary(
        False, "employment", "Частичная занятость"
    )
    assert object_of_comparison[0]["employment"]["name"] == "Частичная занятость"


def test__filtering_vacancies_project(object_filtering_vacancies_defolt):
    object_of_comparison = object_filtering_vacancies_defolt.sorting_vacancies_for_salary(
        False, "employment", "Проектная работа"
    )
    assert object_of_comparison[0]["employment"]["name"] == "Проектная работа"


def test__filtering_vacancies_remout(object_filtering_vacancies_defolt):
    object_of_comparison = object_filtering_vacancies_defolt.sorting_vacancies_for_salary(
        False, "work_format", "Удалённо"
    )
    assert str(object_of_comparison[0]["work_format"]) == """[{'id': 'REMOTE', 'name': 'Удалённо'}]"""


def test__filtering_vacancies_on_site(object_filtering_vacancies_defolt):
    object_of_comparison = object_filtering_vacancies_defolt.sorting_vacancies_for_salary(
        False, "work_format", "На месте работодателя"
    )
    assert str(object_of_comparison[0]["work_format"]) == """[{'id': 'ON_SITE', 'name': 'На месте работодателя'}]"""


def test_shown_object_hh(object_filtering_vacancies_defolt, capsys):
    print(object_filtering_vacancies_defolt)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """
Список вакансий:
1. Python-разработчик 0
2. Backend-разработчик 0
3. Junior Data Engineer 150000
\n"""
    )
