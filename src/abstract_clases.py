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

    def __inpu_data_validation(self):
        pass

    def __call__(self):
        pass

    def vacancy_id(self):
        pass

    def vacancy_salary(self):
        pass

    def vacancy_job_title(self):
        pass

    def vacancy_link_to_vacancy(self):
        pass

    def vacancy_job_requirements(self):
        pass


class Saver:

    def __init__(self):
        pass

    def __str__(self):
        pass

    def save_to_json(self):
        pass

    def load_to_json(self):
        pass

    def cleaning_file(self):
        pass
