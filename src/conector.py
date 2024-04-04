import json
from abc import abstractmethod, ABC


class AbstractConnector(ABC):
    """Абстрактный класс для работы с данными"""

    @abstractmethod
    def add_vacancy(self, job):
        pass

    @abstractmethod
    def get_vacancy(self, count_vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy_id):
        pass


class JsonConnector(AbstractConnector):
    def __init__(self):
        self.data_vacancy = []

    def add_vacancy(self, job):
        """Метод добавления"""
        self.data_vacancy.append(job)

    def get_vacancy(self, count_vacancy):
        """Метод сортировки по количеству №"""
        loaded_vacancies = self.load_file()
        sorted_vacancies = sorted(loaded_vacancies, key=lambda x: x.get('salary', {}).get('from', 0)
        if isinstance(x.get('salary', {}), dict) else 0, reverse=True)
        return sorted_vacancies[:count_vacancy]

    def del_vacancy(self, vacancy):
        """Метод удаления вакансии"""
        self.data_vacancy.remove(vacancy)

    def save_to_file_json(self):
        """Методо сохранения файла"""
        with open('data/vacancy.json', 'w', encoding="utf-8") as file:
            json.dump(self.data_vacancy, file, ensure_ascii=False, indent=4)

    def load_file(self):
        """Метод открытия файла"""
        with open('data/vacancy.json', 'r', encoding="utf-8") as file:
            self.data_vacancy = json.load(file)
            return self.data_vacancy
