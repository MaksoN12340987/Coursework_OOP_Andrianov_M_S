import pytest  # type: ignore

from src.get_api_hh import HH
from src.saver import VacanciSaver
from src.vacancies import VacanciOperator


@pytest.fixture
def object_hh():
    item_test_hh = HH("https://api.hh.ru/vacancies", "Python")
    return item_test_hh


@pytest.fixture
def shown_object_hh() -> str:
    return (
        "https://api.hh.ru/vacancies, {'User-Agent': 'HH-User-Agent'}, {'text': 'Python', 'page': 1, 'per_page': 1}\n"
    )


@pytest.fixture
def object_vacanci_saver():
    save_object = VacanciSaver(
        [
            {
                "id": "119173953",
                "link": "https://hh.ru/vacancy/119173953",
                "name": "QA аналитик / тестировщик (финтех)",
                "salary": "200000",
                "requirements": "Знание SQL, опыт работы с логами. Опыт написания автотестов (Python/JS/Java + Selenium, Playwright, Cypress и т.д.). \n",
            },
            {
                "id": "119151036",
                "link": "https://hh.ru/vacancy/119151036",
                "name": "QA Engineer (middle)",
                "salary": "130000",
                "requirements": "Готовность к инновациям и постоянному профессиональному росту. Ответственность за итоговое качество продукта и готовность принимать решения. Желание развиваться до Fullstack...\n",
            },
        ],
        "test/data_test_vacancies.json",
    )
    return save_object


@pytest.fixture
def vacancies():
    return [
        {
            "id": "119173953",
            "link": "https://hh.ru/vacancy/119173953",
            "name": "QA аналитик / тестировщик (финтех)",
            "salary": "200000",
            "requirements": "Знание SQL, опыт работы с логами. Опыт написания автотестов (Python/JS/Java + Selenium, Playwright, Cypress и т.д.). \n",
        },
        {
            "id": "119151036",
            "link": "https://hh.ru/vacancy/119151036",
            "name": "QA Engineer (middle)",
            "salary": "130000",
            "requirements": "Готовность к инновациям и постоянному профессиональному росту. Ответственность за итоговое качество продукта и готовность принимать решения. Желание развиваться до Fullstack...\n",
        },
    ]


@pytest.fixture
def returnet_of_file():
    return str(
        [
            {
                "id": "119173953",
                "link": "https://hh.ru/vacancy/119173953",
                "name": "QA аналитик / тестировщик (финтех)",
                "salary": "200000",
                "requirements": "Знание SQL, опыт работы с логами. Опыт написания автотестов (Python/JS/Java + Selenium, Playwright, Cypress и т.д.). \n",
            },
            {
                "id": "119151036",
                "link": "https://hh.ru/vacancy/119151036",
                "name": "QA Engineer (middle)",
                "salary": "130000",
                "requirements": "Готовность к инновациям и постоянному профессиональному росту. Ответственность за итоговое качество продукта и готовность принимать решения. Желание развиваться до Fullstack...\n",
            },
        ]
    )


@pytest.fixture
def object_vacanci_operator():
    vacanci_operator = VacanciOperator(
        {
            "id": "119173953",
            "premium": "false",
            "name": "QA аналитик / тестировщик (финтех)",
            "department": "null",
            "has_test": "false",
            "response_letter_required": "false",
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": {"from": 200000, "to": 160000, "currency": "RUR", "gross": "false"},
            "salary_range": "null",
            "type": {"id": "open", "name": "Открытая"},
            "address": "null",
            "response_url": "null",
            "sort_point_distance": "null",
            "published_at": "2025-04-03T15:19:36+0300",
            "created_at": "2025-04-03T15:19:36+0300",
            "archived": "false",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=119126777",
            "show_logo_in_search": "null",
            "insider_interview": "null",
            "url": "https://api.hh.ru/vacancies/119126777?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/119173953",
            "relations": [],
            "employer": {
                "id": "5550364",
                "name": "Marfatech",
                "url": "https://api.hh.ru/employers/5550364",
                "alternate_url": "https://hh.ru/employer/5550364",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/947617.png",
                    "90": "https://img.hhcdn.ru/employer-logo/4231004.png",
                    "240": "https://img.hhcdn.ru/employer-logo/4231005.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=5550364",
                "accredited_it_employer": "false",
                "trusted": "true",
            },
            "snippet": {
                "requirement": "Знание SQL, опыт работы с логами.",
                "responsibility": "Тестирование UI/UX. Тестирование компонентов UI Kit.",
            },
            "show_contacts": "false",
            "contacts": "null",
            "schedule": {"id": "remote", "name": "Удаленная работа"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": "false",
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "REMOTE", "name": "Удалённо"}],
            "working_hours": [{"id": "HOURS_9", "name": "9 часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": "false",
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": "false",
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": "false",
            "adv_response_url": "null",
            "is_adv_vacancy": "false",
            "adv_context": "null",
        }
    )
    return vacanci_operator


@pytest.fixture
def object_empty_vacanci_operator():
    vacanci_operator = VacanciOperator({})
    return vacanci_operator


@pytest.fixture
def object_of_comparison_vacanci_operator():
    comparison_vacanci_operator = VacanciOperator(
        {
            "id": "119173922",
            "premium": "false",
            "name": "QA аналитик / тестировщик (финтех)",
            "department": "null",
            "has_test": "false",
            "response_letter_required": "false",
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": {"from": 150000, "to": 160000, "currency": "RUR", "gross": "false"},
            "salary_range": "null",
            "type": {"id": "open", "name": "Открытая"},
            "address": "null",
            "response_url": "null",
            "sort_point_distance": "null",
            "published_at": "2025-04-03T15:19:36+0300",
            "created_at": "2025-04-03T15:19:36+0300",
            "archived": "false",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=119126777",
            "show_logo_in_search": "null",
            "insider_interview": "null",
            "url": "https://api.hh.ru/vacancies/119126777?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/119173953",
            "relations": [],
            "employer": {
                "id": "5550364",
                "name": "Marfatech",
                "url": "https://api.hh.ru/employers/5550364",
                "alternate_url": "https://hh.ru/employer/5550364",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/947617.png",
                    "90": "https://img.hhcdn.ru/employer-logo/4231004.png",
                    "240": "https://img.hhcdn.ru/employer-logo/4231005.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=5550364",
                "accredited_it_employer": "false",
                "trusted": "true",
            },
            "snippet": {
                "requirement": "Знание SQL, опыт работы с логами.",
                "responsibility": "Тестирование UI/UX. Тестирование компонентов UI Kit.",
            },
            "show_contacts": "false",
            "contacts": "null",
            "schedule": {"id": "remote", "name": "Удаленная работа"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": "false",
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "REMOTE", "name": "Удалённо"}],
            "working_hours": [{"id": "HOURS_9", "name": "9 часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": "false",
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": "false",
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": "false",
            "adv_response_url": "null",
            "is_adv_vacancy": "false",
            "adv_context": "null",
        }
    )
    return comparison_vacanci_operator
