import json
from abc import ABC, abstractmethod
import requests


class JobAPI(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacantion(self):
        pass


class WorkinHH(JobAPI):
    """Класс для работы с поступающими данными с api"""
    def connect(self):
        """ Метод информации о подключении """
        if self.get_vacantion():
            print('Подключение выполнено')
        else:
            print('Ошибка с подключением')

    def get_vacantion(self):
        """ Метод получения данных """
        responce = requests.get('https://api.hh.ru/vacancies')
        if responce.status_code == 200:
            return responce.json()
        else:
            print(f'Возникла ошибка {responce.status_code}')
            return None

    def save_file_vacantion(self):
        """ Метод сохранения данных в файле """
        data_vacantion = WorkinHH.get_vacantion(self)
        with open('vacantion.json', 'w', encoding="utf-8") as file:
            json.dump(data_vacantion, file, ensure_ascii=False, indent=4)

    @staticmethod
    def open_file():
        """ Метод получения данных из json """
        with open('vacantion.json', 'r', encoding="utf-8") as data:
            data_vacantion = json.load(data)
            return data_vacantion['items']


hh = WorkinHH()
print(hh.connect())
print(hh.get_vacantion())
print(hh.save_file_vacantion())
for i in hh.open_file():
    print(i)

