import pytest
from datetime import datetime

@pytest.fixture
def info():
    return {'category': 'FOO', 'description': 'This is FOO'}


@pytest.fixture
def test_dict_base(info):
    return {'foo': {'bar': 'BAR'}}


@pytest.fixture
def test_dict(info):
    return {
        'foo': [
            {
                'code': 123, 
                'date_prod': datetime(2023, 1, 1, 10, 14, 0),
                'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
                'info': info
            },
            {
                'code': 123, 
                'date_prod': datetime(2023, 1, 1, 10, 16, 0),
                'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
                'info': info
            },
            {
                'code': 123, 
                'date_prod': datetime(2023, 1, 1, 10, 22, 0),
                'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
                'info': info
            },
            
        ],

        'bar': [
            {
                'code': 123, 
                'date_prod': datetime(2023, 1, 1, 10, 14, 0),
                'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
                'info': None
            },
        ],

        'fizz': []
    }


@pytest.fixture
def test_list_base():
    return [{'info': {'name': 'FOO'}}, {'info': {'name': 'BAR'}}, {'info': {'name': 'FIZZ'}}]