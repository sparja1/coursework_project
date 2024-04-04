from abc import ABC, abstractmethod
import requests


class ApiJobAbstract(ABC):
    """Абстрактный класс для работы с платформой hh"""

    @abstractmethod
    def get_vacancy_api(self, keyword):
        pass


class ApiJob(ApiJobAbstract):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancy_api(self, keyword):
        """Метод для поиска выкансий"""
        self.params['text'] = keyword
        while self.params.get('page') != 2:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
