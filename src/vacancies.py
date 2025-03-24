from src.abstract_clases import Vacanci


class VacanciOperator(Vacanci):
    pull_vacanci: list

    def __init__(self, pull_vacanci):
        self.__job_title = ""
        self.__job_title = ""
        self.__pull_vacanci = pull_vacanci
        self.__job_link = pull_vacanci
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
