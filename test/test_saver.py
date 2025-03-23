from unittest.mock import patch

from src.saver import Saver


def test_load_vacancy(object_saver, vacancies):
    save_object = Saver("data/vacancies_hh.json")
    assert object_saver.save_vacancy(vacancies) == "Write vacancies OK"
