import pytest


# Positive tests
def test_save_vacancy(object_saver, vacancies):
    assert object_saver.save_vacancy(vacancies) == "Write vacancies OK"


def test_load_vacancy(object_saver, returnet_of_file):
    assert str(object_saver.load_vacancy()) == returnet_of_file


# Negative tests
def test_save_vacancy_error(object_saver, vacancies):
    with pytest.raises(PermissionError):
        assert (
            object_saver.save_vacancy(vacancies, ".......")
            == "Error! Access denied or file with such name cannot be created"
        )


def test_load_vacancy_error(object_saver):
    with pytest.raises(PermissionError):
        assert (
            object_saver.load_vacancy(".......")
            == "File access error"
        )


def test_load_vacancy_file_not_found(object_saver, capsys):
    assert object_saver.load_vacancy("data_test_vacancies.json") == []
    captured = capsys.readouterr()
    assert captured.out == "Error, file not found\n"
