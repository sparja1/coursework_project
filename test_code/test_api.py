import pytest
from unittest.mock import patch

from src.api import ApiJob


@pytest.fixture
def api_job_instance():
    return ApiJob()

def test_init(api_job_instance):
    assert api_job_instance.url == 'https://api.hh.ru/vacancies'
    assert api_job_instance.headers == {'User-Agent': 'HH-User-Agent'}
    assert api_job_instance.params == {'text': '', 'page': 0, 'per_page': 100}
    assert api_job_instance.vacancies == []
