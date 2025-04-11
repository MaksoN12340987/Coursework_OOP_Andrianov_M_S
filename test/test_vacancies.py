# Positive tests
def test_save_vacancy(object_vacanci_operator):
    assert object_vacanci_operator.vacancy_id == "id вакансии:\n119173953"
    assert object_vacanci_operator.vacancy_salary == "Зарплата:\n200000"
    assert object_vacanci_operator.vacancy_job_title == "Должность:\nQA аналитик / тестировщик (финтех)"
    assert object_vacanci_operator.vacancy_link_to_vacancy == "Ссылка на вакансию:\nhttps://hh.ru/vacancy/119173953"
    assert (
        object_vacanci_operator.vacancy_job_requirements
        == "Требоапния к соискателю:\nЗнание SQL, опыт работы с логами.\n"
    )


def test_call_save_vacancy(object_vacanci_operator):
    assert object_vacanci_operator() == {
        "id": "119173953",
        "link": "https://hh.ru/vacancy/119173953",
        "name": "QA аналитик / тестировщик (финтех)",
        "salary": "200000",
        "requirements": "Знание SQL, опыт работы с логами.\n",
    }


def test_empty_save_vacancy(object_empty_vacanci_operator):
    assert object_empty_vacanci_operator() == {
        "id": 0,
        "link": "",
        "name": "",
        "salary": 0,
        "requirements": "",
    }


def test_save_vacancy_comparison(object_vacanci_operator, object_of_comparison_vacanci_operator):
    assert str(object_vacanci_operator == object_of_comparison_vacanci_operator) == "False"
    assert str(object_vacanci_operator < object_of_comparison_vacanci_operator) == "False"
    assert str(object_vacanci_operator > object_of_comparison_vacanci_operator) == "True"


def test_save_vacancy_str(object_vacanci_operator, capsys):
    print(object_vacanci_operator)
    captured = capsys.readouterr()
    assert captured.out == "200000\n"


def test_save_vacancy_sorting(object_vacanci_operator, object_vacanci_saver, capsys):
    object_vacanci_operator.sorting_vacancies_for_salary(
        object_vacanci_saver.load_to_json("log/intermediate_result.json"), False, "", ""
    )
    captured = capsys.readouterr()
    assert captured.out == "Параметр  не найден\n"


def test_save_vacancy_sorting_employment(object_vacanci_operator, object_vacanci_saver, capsys):
    result = object_vacanci_operator.sorting_vacancies_for_salary(
        object_vacanci_saver.load_to_json("log/intermediate_result.json"), False, "employment", "Вахта"
    )
    assert len(result) == 1
    assert result[0]["employment"]["name"] == "Вахта"


def test_save_vacancy_sorting_work_format(object_vacanci_operator, object_vacanci_saver, capsys):
    result = object_vacanci_operator.sorting_vacancies_for_salary(
        object_vacanci_saver.load_to_json("log/intermediate_result.json"), False, "work_format", "Удалённо"
    )
    assert len(result) == 1
    assert result[0]["work_format"][0]["id"] == "REMOTE"
