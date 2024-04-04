class VacancyHH:
    """Класс для работы с вакансиями"""

    def __init__(self, name_vacancy: str, link_vacancy: str, salary: int, short_description: str, requirements: str):
        self.name_vacancy = name_vacancy
        self.link_vacancy = link_vacancy
        self.salary = salary if salary else 0
        self.short_description = short_description if short_description else 'Краткое описание не указаны'
        self.requirements = requirements if requirements else 'Требования не указаны'

    def __lt__(self, other):
        """Метод стравнения"""
        if isinstance(self.salary, dict) and isinstance(other.salary, dict):
            return self.salary.get('from', 0) < other.salary.get('from', 0)
        return False

    def to_dict(self):
        """Метод возвращает словарь который можно добавить"""
        data_vacancy = {
            'name_vacancy': self.name_vacancy,
            'link_vacancy': self.link_vacancy,
            'salary': self.salary,
            'short_description': self.short_description,
            'requirements': self.requirements}
        return data_vacancy
