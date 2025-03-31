from abc import ABC, abstractmethod


class Parser(ABC):

    def __init__(self):
        pass

    def __str__(self):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass


class Vacanci(ABC):

    def __init__(self):
        pass

    def __str__(self):
        pass

    def vacancy_job_title(self):
        pass

    def vacancy_link_to_vacancy(self):
        pass

    def vacancy_salary(self):
        pass

    def vacancy_job_requirements(self):
        pass

    def sorting_vacancies_for_salary(self):
        pass

    def filtering_vacancies(self):
        pass
