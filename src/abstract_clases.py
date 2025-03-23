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
