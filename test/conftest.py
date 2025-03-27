import pytest

from src.filtering_vacancies import FilteringVacancies
from src.get_api_hh import HH
from src.saver import VacanciSaver
from src.vacancies import VacanciOperator


@pytest.fixture
def object_hh():
    item_test_hh = HH("https://api.hh.ru/vacancies", "Python")
    return item_test_hh


@pytest.fixture
def object_vacanci_saver():
    save_object = VacanciSaver("test/data_test_vacancies.json")
    return save_object


@pytest.fixture
def object_vacanci_operator(object_vacanci_saver):
    object_vacanci = VacanciOperator(object_vacanci_saver.load_vacancy("test/data_test_vacancies.json"))
    return object_vacanci


@pytest.fixture
def object_vacanci_operator_list_clear():
    object_vacanci = VacanciOperator([])
    return object_vacanci


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
            "premium": False,
            "name": "Golang Developer",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "1006", "name": "Гродно", "url": "https://api.hh.ru/areas/1006"},
            "salary": None,
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-03-18T17:27:48+0300",
            "created_at": "2025-03-18T17:27:48+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=118520774",
            "show_logo_in_search": None,
            "insider_interview": None,
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
                    "240": "https://img.hhcdn.ru/employer-logo/1089726.jpeg",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=972978",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "2+ года коммерческого опыта с Golang. Английский В1. Хорошее понимание микросервисной архитектуры. Владение стеком: Go, gRPC, GraphQL, HTTP...",
                "responsibility": "Проектированием архитектуры приложений. Разработкой микросервисов и монолитов. Код ревью. Планированием задач.",
            },
            "show_contacts": True,
            "contacts": None,
            "schedule": {"id": "remote", "name": "Удаленная работа"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": True,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "REMOTE", "name": "Удалённо"}],
            "working_hours": [{"id": "HOURS_8", "name": "8 часов"}],
            "work_schedule_by_days": [
                {"id": "FIVE_ON_TWO_OFF", "name": "5/2"},
                {"id": "FLEXIBLE", "name": "Свободный"},
            ],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
        {
            "id": "118676373",
            "premium": False,
            "name": "Тестировщик",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": {"from": 100000, "to": None, "currency": "RUR", "gross": False},
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Москва",
                "street": "2-я Брестская улица",
                "building": "6",
                "lat": 55.770841,
                "lng": 37.591207,
                "description": None,
                "raw": "Москва, 2-я Брестская улица, 6",
                "metro": None,
                "metro_stations": [],
                "id": "17852661",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-03-23T15:48:28+0300",
            "created_at": "2025-03-23T15:48:28+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=118676373",
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/118676373?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/118676373",
            "relations": [],
            "employer": {
                "id": "11858800",
                "name": "Цифролаб",
                "url": "https://api.hh.ru/employers/11858800",
                "alternate_url": "https://hh.ru/employer/11858800",
                "logo_urls": None,
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=11858800",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Понимание основных принципов REST API, базовое знание HTTP. Начальное знание <highlighttext>Python</highlighttext> (понимание таких тем, как: условные операторы, циклы, методы строк...",
                "responsibility": "Тестировать API, backend, frontend, требования UX|UI ПО. Анализировать данные веб-трафика (логи). Подготавливать тестовые данные. Настраивать тестовое окружение. ",
            },
            "show_contacts": False,
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "ON_SITE", "name": "На месте работодателя"}, {"id": "HYBRID", "name": "Гибрид"}],
            "working_hours": [{"id": "HOURS_8", "name": "8 часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "124", "name": "Тестировщик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
    ]


@pytest.fixture
def object_object_vacanci_operator_salary(vacancies):
    save_object = VacanciOperator(
        [
            {
                "id": "118520774",
                "premium": False,
                "name": "Golang Developer",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "1006", "name": "Гродно", "url": "https://api.hh.ru/areas/1006"},
                "salary": None,
                "alternate_url": "https://hh.ru/vacancy/118728255",
                "snippet": {
                    "requirement": "Опыт работы числовым аналитиком от 2 лет. Уверенное знание <highlighttext>Python</highlighttext>"
                    + ", SQL. Понимание основ теории вероятностей и мат.статистики. Уже работал с...",
                    "responsibility": "Планировать KPI. Разрабатывать модели прогнозирований. Проводить исследования, сопровождать А/В тесты. "
                    + "Разрабатывать отчетность, дашборды. Анализировать и предлагать решения по повышению...",
                },
            },
            {
                "id": "118676373",
                "premium": False,
                "name": "Тестировщик",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
                "salary": {"from": 100000, "to": None, "currency": "RUR", "gross": False},
                "alternate_url": "https://hh.ru/vacancy/118728255",
                "snippet": {
                    "requirement": "Опыт работы числовым аналитиком от 2 лет. Уверенное знание <highlighttext>Python</highlighttext>, "
                    + "SQL. Понимание основ теории вероятностей и мат.статистики. Уже работал с...",
                    "responsibility": "Планировать KPI. Разрабатывать модели прогнозирований. Проводить исследования, сопровождать А/В тесты. "
                    + "Разрабатывать отчетность, дашборды. Анализировать и предлагать решения по повышению...",
                },
            },
        ]
    )
    return save_object


@pytest.fixture
def returnet_of_file():
    return str(
        [
            {
                "id": "118520774",
                "premium": False,
                "name": "Golang Developer",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "1006", "name": "Гродно", "url": "https://api.hh.ru/areas/1006"},
                "salary": None,
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2025-03-18T17:27:48+0300",
                "created_at": "2025-03-18T17:27:48+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=118520774",
                "show_logo_in_search": None,
                "insider_interview": None,
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
                        "240": "https://img.hhcdn.ru/employer-logo/1089726.jpeg",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=972978",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "2+ года коммерческого опыта с Golang. Английский В1. Хорошее понимание микросервисной архитектуры. "
                    + "Владение стеком: Go, gRPC, GraphQL, HTTP...",
                    "responsibility": "Проектированием архитектуры приложений. Разработкой микросервисов и монолитов. Код ревью. "
                    + "Планированием задач.",
                },
                "show_contacts": True,
                "contacts": None,
                "schedule": {"id": "remote", "name": "Удаленная работа"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": True,
                "fly_in_fly_out_duration": [],
                "work_format": [{"id": "REMOTE", "name": "Удалённо"}],
                "working_hours": [{"id": "HOURS_8", "name": "8 часов"}],
                "work_schedule_by_days": [
                    {"id": "FIVE_ON_TWO_OFF", "name": "5/2"},
                    {"id": "FLEXIBLE", "name": "Свободный"},
                ],
                "night_shifts": False,
                "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
                "accept_incomplete_resumes": False,
                "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "employment_form": {"id": "FULL", "name": "Полная"},
                "internship": False,
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
            {
                "id": "118676373",
                "premium": False,
                "name": "Тестировщик",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
                "salary": {"from": 100000, "to": None, "currency": "RUR", "gross": False},
                "type": {"id": "open", "name": "Открытая"},
                "address": {
                    "city": "Москва",
                    "street": "2-я Брестская улица",
                    "building": "6",
                    "lat": 55.770841,
                    "lng": 37.591207,
                    "description": None,
                    "raw": "Москва, 2-я Брестская улица, 6",
                    "metro": None,
                    "metro_stations": [],
                    "id": "17852661",
                },
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2025-03-23T15:48:28+0300",
                "created_at": "2025-03-23T15:48:28+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=118676373",
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/118676373?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/118676373",
                "relations": [],
                "employer": {
                    "id": "11858800",
                    "name": "Цифролаб",
                    "url": "https://api.hh.ru/employers/11858800",
                    "alternate_url": "https://hh.ru/employer/11858800",
                    "logo_urls": None,
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=11858800",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Понимание основных принципов REST API, базовое знание HTTP. Начальное знание <highlighttext>Python"
                    + "</highlighttext> (понимание таких тем, как: условные операторы, циклы, методы строк...",
                    "responsibility": "Тестировать API, backend, frontend, требования UX|UI ПО. Анализировать данные веб-трафика (логи). "
                    + "Подготавливать тестовые данные. Настраивать тестовое окружение. ",
                },
                "show_contacts": False,
                "contacts": None,
                "schedule": {"id": "fullDay", "name": "Полный день"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "fly_in_fly_out_duration": [],
                "work_format": [
                    {"id": "ON_SITE", "name": "На месте работодателя"},
                    {"id": "HYBRID", "name": "Гибрид"},
                ],
                "working_hours": [{"id": "HOURS_8", "name": "8 часов"}],
                "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
                "night_shifts": False,
                "professional_roles": [{"id": "124", "name": "Тестировщик"}],
                "accept_incomplete_resumes": False,
                "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "employment_form": {"id": "FULL", "name": "Полная"},
                "internship": False,
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
        ]
    )


@pytest.fixture
def sorted_vacancies():
    return [
        {
            "id": "118676373",
            "premium": False,
            "name": "Тестировщик",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": {"from": 100000, "to": None, "currency": "RUR", "gross": False},
            "alternate_url": "https://hh.ru/vacancy/118728255",
            "snippet": {
                "requirement": "Опыт работы числовым аналитиком от 2 лет. Уверенное знание <highlighttext>Python"
                + "</highlighttext>, SQL. Понимание основ теории вероятностей и мат.статистики. Уже работал с...",
                "responsibility": "Планировать KPI. Разрабатывать модели прогнозирований. Проводить исследования, сопровождать А/В тесты. "
                + "Разрабатывать отчетность, дашборды. Анализировать и предлагать решения по повышению...",
            },
        },
        {
            "id": "118520774",
            "premium": False,
            "name": "Golang Developer",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "1006", "name": "Гродно", "url": "https://api.hh.ru/areas/1006"},
            "salary": {
                "from": 0,
            },
            "alternate_url": "https://hh.ru/vacancy/118728255",
            "snippet": {
                "requirement": "Опыт работы числовым аналитиком от 2 лет. Уверенное знание <highlighttext>Python</highlighttext>, SQL. "
                + "Понимание основ теории вероятностей и мат.статистики. Уже работал с...",
                "responsibility": "Планировать KPI. Разрабатывать модели прогнозирований. Проводить исследования, сопровождать А/В тесты. "
                + "Разрабатывать отчетность, дашборды. Анализировать и предлагать решения по повышению...",
            },
        },
    ]


@pytest.fixture
def return_vacancy_job_requirements() -> str:
    return "2+ года коммерческого опыта с Golang. Английский В1. Хорошее понимание микросервисной архитектуры. Владение стеком: Go, gRPC, GraphQL, HTTP...\n"


@pytest.fixture
def object_filtering_vacancies_defolt():
    object_vacanci = VacanciSaver("test/data_test_filters.json")
    object_filtering_vacancies = FilteringVacancies(object_vacanci.load_vacancy())
    return object_filtering_vacancies
