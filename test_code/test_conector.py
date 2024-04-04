

from src.conector import JsonConnector


def test_JsonConnector_init():
    connector = JsonConnector()
    assert connector.data_vacancy == []


def test_JsonConnector_add_vacancy():
    connector = JsonConnector()
    job = {'name': 'Test Job', 'salary': 1000}
    connector.add_vacancy(job)
    assert connector.data_vacancy == [job]

def test_JsonConnector_del_vacancy():
    connector = JsonConnector()
    job = {'name': 'Test Job', 'salary': 1000}
    connector.data_vacancy.append(job)
    connector.del_vacancy(job)
    assert connector.data_vacancy == []