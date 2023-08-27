import pytest
from src import SafeDict, SafeSequence, SafeNone


def test_get_attribute(test_dict_base):
    value = SafeDict(**test_dict_base) >> 'foo' >> 'bar'
    value2 = SafeDict(**test_dict_base) >> 'foo' >= 'bar'

    assert isinstance(value, str), f'The object must be a str instance!'
    assert isinstance(value2, str), f'The object must be a str instance!'
    assert value == 'BAR', 'Bad results for value'
    assert value2 == 'BAR', 'Bad results for value2'
    


def test_get_safe_dict(test_dict_base):
    value = SafeDict(**test_dict_base) >> 'foo'

    assert isinstance(value, SafeDict), f'The object must be a SafeDict instance!'
    assert value == SafeDict(**test_dict_base['foo']), 'Bad results'



def test_get_dict(test_dict_base):
    value = SafeDict(**test_dict_base) >= 'foo'

    assert isinstance(value, dict), f'The object must be a dict instance!'
    assert value == test_dict_base['foo'], 'Bad results'



def test_get_complex_safe_attribute(test_dict, info):
    value = SafeDict(**test_dict) >> 'foo' >> [0] >> 'info'

    assert isinstance(value, SafeDict), f'The object must be a SafeDict instance!'
    assert value == SafeDict(**info), 'Bad results'



def test_get_complex_attribute(test_dict, info):
    value = SafeDict(**test_dict) >> 'foo' >> [0] >= 'info'

    assert isinstance(value, dict), f'The object must be a dict instance!'
    assert value == info, 'Bad results'


def test_get_multiple_safe_attribute(test_dict, info):
    value = SafeDict(**test_dict) >> 'foo' >> [0] >> 'info'
    value2 = value >> 'category'

    assert isinstance(value, SafeDict), 'The object must be a SafeDict instance!'
    assert value == SafeDict(**info), 'Bad results'
    assert isinstance(value2, str), f'The object must be a str instance!'
    assert value2 == 'FOO', 'Bad results for value2'



def test_get_none_attribute(test_dict):
    value = SafeDict(**test_dict) >> 'bar' >> [0] >> 'info'
    value2 = SafeDict(**test_dict) >> 'bar' >> [0] >= 'info'

    assert isinstance(value, SafeNone), 'The object must be a SafeNone instance!'
    assert value2 is None, 'Bad results'



def test_manage_none_results(test_dict):
    value = SafeDict(**test_dict) >> 'bar' >> [0] >> 'info' >> 'category'
    value2 = SafeDict(**test_dict) >> 'bar' >> [0] >> 'info' >= 'category'

    assert isinstance(value, SafeNone), 'The object must be a SafeNone instance!'
    assert value2 is None, 'Bad results'