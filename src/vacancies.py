from src.abstract_clases import Vacanci


class VacanciOperator(Vacanci):
    pull_vacanci: list

    def __init__(self, pull_vacanci):
        self.__job_title = ""
        self.__link_to_vacancy = ""
        self.__salary = 0
        self.__job_requirements = ""
        self.__pull_vacanci = pull_vacanci
        super().__init__()

    def __str__(self):
        super().__str__()
        result = "\nСписок вакансий:\n"
        for i, value in enumerate(self.pull_vacanci):
            result += f"{i+1}. {value["name"]}\n"
        
        if len(self.pull_vacanci) < 1:
            result += "Упс, вакансий не нашлось("
        
        return result

    def sorting_vacancies(self, sort_selector):
        keys = ["name", "", "", "salary", "requirement"]
