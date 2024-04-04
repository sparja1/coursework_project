from src.vacancy import VacancyHH
import pytest


def test_VacancyHH_init():
    vacancy = VacancyHH('Test Vacancy', 'https://test.link', 1000, 'Test description', 'Test requirements')
    assert vacancy.name_vacancy == 'Test Vacancy'
    assert vacancy.link_vacancy == 'https://test.link'
    assert vacancy.salary == 1000
    assert vacancy.short_description == 'Test description'
    assert vacancy.requirements == 'Test requirements'


def test_VacancyHH_lt():
    vacancy1 = VacancyHH('Test Vacancy 1', 'https://test.link', {'from': 1000}, 'Test description', 'Test requirements')
    vacancy2 = VacancyHH('Test Vacancy 2', 'https://test.link', {'from': 2000}, 'Test description', 'Test requirements')
    assert (vacancy1 < vacancy2)


def test_VacancyHH_to_dict():
    vacancy = VacancyHH('Test Vacancy', 'https://test.link', 1000, 'Test description', 'Test requirements')
    expected_dict = {
        'name_vacancy': 'Test Vacancy',
        'link_vacancy': 'https://test.link',
        'salary': 1000,
        'short_description': 'Test description',
        'requirements': 'Test requirements'
    }
    assert vacancy.to_dict() == expected_dict
