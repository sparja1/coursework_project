from src.conector import JsonConnector
from src.api import ApiJob
from src.vacancy import VacancyHH
import os

def main():
    """Функция взаимодествия с пользователем"""
    directory = 'data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    api = ApiJob()
    json_connector = JsonConnector()
    name_vacancy_input = input("Введите ключевое слово для поиска вакансий: ")
    count_vacancy = int(input('Введите сколько вакансий вывести по зарплате: '))
    api.get_vacancy_api(name_vacancy_input)

    for i in api.vacancies:
        salary_from = i['salary']['from'] if i['salary'] is not None else None
        vacancy = VacancyHH(i['name'], i['area']['url'], salary_from,
                            i['snippet']['responsibility'], i['snippet'].get('requirements', 'Требования не указаны'))

        json_connector.add_vacancy(vacancy.to_dict())

    json_connector.save_to_file_json()
    for i in json_connector.get_vacancy(count_vacancy):
        print(f"Название {i['name_vacancy']}")
        print(f"Ссылка на вакансию {i['link_vacancy']}")
        print(f"Зарплата {i['salary']}")
        print(f"Краткое описание {i['short_description']}")
        print(f"Требования {i['requirements']}")
        print()



if __name__ == "__main__":
    main()
