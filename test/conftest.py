import pytest
from datetime import datetime

@pytest.fixture
def info_foo():
    return {'category': 'FOO', 'description': 'This is FOO'}


@pytest.fixture
def info_bar():
    return {'category': 'BAR', 'description': 'This is BAR'}


@pytest.fixture
def info_fizz():
    return {'category': 'FIZZ', 'description': 'This is FIZZ'}


@pytest.fixture
def test_dict_base():
    return {'foo': {'bar': 'BAR'}}


@pytest.fixture
def test_dict(info_foo, info_bar, info_fizz):
    return {
        'foo': [
            {
                'code': 123, 
                'date_prod': datetime(2023, 1, 1, 10, 14, 0),
                'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
                'info': info_foo
            },
            {
                'code': 234, 
                'date_prod': datetime(2023, 1, 1, 10, 16, 0),
                'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
                'info': info_bar
            },
            {
                'code': 345, 
                'date_prod': datetime(2023, 1, 1, 10, 22, 0),
                'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
                'info': info_fizz
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
def test_list_base(info_foo, info_bar, info_fizz):
    return [info_foo, info_bar, info_fizz]


@pytest.fixture
def test_list_complex(info_foo, info_bar, info_fizz):
    return [
        [
            info_foo,
            info_foo,
            info_foo,
        ],
        [
            info_bar,
            info_bar,
            info_bar,
        ],
        [
            info_fizz,
            info_fizz,
            info_fizz,
        ]
    ]
