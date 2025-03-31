# import json
# from unittest.mock import patch

import pytest

from src.get_api_hh import HH


def test_shown_object_hh(shown_object_hh, object_hh, capsys):
    print(object_hh)
    captured = capsys.readouterr()
    assert captured.out == shown_object_hh


def test_conection_error():
    object_hh = HH("https://api.hh.r", "Python")
    with pytest.raises(ConnectionError):
        assert object_hh.load_vacancies == "Connection Error. Please check your network connection."


def test_url_error():
    object_hh = HH("https://api.hh.ru", "Python")
    with pytest.raises(ValueError):
        assert object_hh.load_vacancies == "HTTP Error. Please check the URL."
