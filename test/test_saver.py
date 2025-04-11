import pytest  # type: ignore


# Positive tests
def test_load_vacancy_str(object_vacanci_saver, capsys):
    print(object_vacanci_saver)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """
Список вакансий:
1. QA аналитик / тестировщик (финтех)
2. QA Engineer (middle)

"""
    )


def test_save_vacancy(object_vacanci_saver):
    assert object_vacanci_saver.save_to_json("test/data_test_vacancies.json") == "Write vacancies OK"


def test_save_vacancy_empti_file(object_vacanci_saver):
    assert object_vacanci_saver.save_to_json("test/data_test_clear.json") == "Write vacancies OK"


def test_load_vacancy(object_vacanci_saver, returnet_of_file):
    assert str(object_vacanci_saver.load_to_json("test/data_test_vacancies.json")) == returnet_of_file


def test_cleaning_file(object_vacanci_saver):
    assert object_vacanci_saver.cleaning_file("test/data_test_clear.json") == "Clear vacancies OK"


def test_save_vacancy_not_path(object_vacanci_saver):
    assert object_vacanci_saver.save_to_json() == "Write vacancies OK"


def test_load_vacancy_not_path(object_vacanci_saver, returnet_of_file):
    assert str(object_vacanci_saver.load_to_json()) == returnet_of_file


# Negative tests
def test_save_vacancy_error(object_vacanci_saver):
    with pytest.raises(PermissionError):
        assert (
            object_vacanci_saver.save_to_json(".......")
            == "Error! Access denied or file with such name cannot be created"
        )


def test_load_vacancy_error(object_vacanci_saver):
    with pytest.raises(PermissionError):
        assert object_vacanci_saver.load_to_json(".......") == "File access error"


def test_load_vacancy_file_not_found(object_vacanci_saver, capsys):
    assert object_vacanci_saver.load_to_json("data_test_vacancies.json") == []
    captured = capsys.readouterr()
    assert captured.out == "Error, file not found\n"


def test_cleaning_file_file_premission(object_vacanci_saver):
    with pytest.raises(PermissionError):
        assert object_vacanci_saver.cleaning_file(".......") == "File access error"
