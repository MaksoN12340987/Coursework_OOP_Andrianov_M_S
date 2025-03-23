import json

import pytest

from src.saver import Saver
from src.get_api_hh import HH


@pytest.fixture
def object_hh():
    item_test_hh = HH("https://api.hh.ru/vacancies", "Python")
    return item_test_hh


@pytest.fixture
def object_saver():
    save_object = Saver("test/data_test_vacancies.json")
    return save_object


@pytest.fixture
def shown_object_hh() -> str:
    return (
        "https://api.hh.ru/vacancies, {'User-Agent': 'HH-User-Agent'}, {'text': 'Python', 'page': 1, 'per_page': 1}\n"
    )


@pytest.fixture
def vacancies():
    return [
    {
        "id": "118520774",
        "premium": "false",
        "name": "Golang Developer",
        "department": "null",
        "has_test": "false",
        "response_letter_required": "false",
        "area": {
            "id": "1006",
            "name": "Гродно",
            "url": "https://api.hh.ru/areas/1006"
        },
        "salary": "null",
        "type": {
            "id": "open",
            "name": "Открытая"
        },
        "address": "null",
        "response_url": "null",
        "sort_point_distance": "null",
        "published_at": "2025-03-18T17:27:48+0300",
        "created_at": "2025-03-18T17:27:48+0300",
        "archived": "false",
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=118520774",
        "show_logo_in_search": "null",
        "insider_interview": "null",
        "url": "https://api.hh.ru/vacancies/118520774?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/118520774",
        "relations": [],
        "employer": {
            "id": "972978",
            "name": "Фингерз Медиа",
            "url": "https://api.hh.ru/employers/972978",
            "alternate_url": "https://hh.ru/employer/972978",
            "logo_urls": {
                "original": "https://img.hhcdn.ru/employer-logo-original/102338.jpg",
                "90": "https://img.hhcdn.ru/employer-logo/1089725.jpeg",
                "240": "https://img.hhcdn.ru/employer-logo/1089726.jpeg"
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=972978",
            "accredited_it_employer": "false",
            "trusted": "true"
        },
        "snippet": {
            "requirement": "2+ года коммерческого опыта с Golang. Английский В1. Хорошее понимание микросервисной архитектуры. Владение стеком: Go, gRPC, GraphQL, HTTP...",
            "responsibility": "Проектированием архитектуры приложений. Разработкой микросервисов и монолитов. Код ревью. Планированием задач."
        },
        "show_contacts": "true",
        "contacts": "null",
        "schedule": {
            "id": "remote",
            "name": "Удаленная работа"
        },
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": "true",
        "fly_in_fly_out_duration": [],
        "work_format": [
            {
                "id": "REMOTE",
                "name": "Удалённо"
            }
        ],
        "working_hours": [
            {
                "id": "HOURS_8",
                "name": "8 часов"
            }
        ],
        "work_schedule_by_days": [
            {
                "id": "FIVE_ON_TWO_OFF",
                "name": "5/2"
            },
            {
                "id": "FLEXIBLE",
                "name": "Свободный"
            }
        ],
        "night_shifts": "false",
        "professional_roles": [
            {
                "id": "96",
                "name": "Программист, разработчик"
            }
        ],
        "accept_incomplete_resumes": "false",
        "experience": {
            "id": "between1And3",
            "name": "От 1 года до 3 лет"
        },
        "employment": {
            "id": "full",
            "name": "Полная занятость"
        },
        "employment_form": {
            "id": "FULL",
            "name": "Полная"
        },
        "internship": "false",
        "adv_response_url": "null",
        "is_adv_vacancy": "false",
        "adv_context": "null"
    }
]
