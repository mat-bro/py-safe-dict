from ..src import safe, SafeDict, SafeSequence


def test_safe_func_on_dict(test_dict, info_foo):
    value = safe(test_dict) >> 'foo' >> [0] >> 'info'
    value2 = value >> 'category'

    assert isinstance(value, SafeDict), 'The object must be a SafeDict instance!'
    assert value == SafeDict(**info_foo), 'Bad results'
    assert isinstance(value2, str), f'The object must be a str instance!'
    assert value2 == 'FOO', 'Bad results for value2'


def test_safe_func_on_sequence(test_list_base):
    value = safe(test_list_base) >> [2] >> 'category'
    value2 = safe(test_list_base) >> [2] >= 'category'

    assert isinstance(value, str), f'The object must be a str instance!'
    assert isinstance(value2, str), f'The object must be a str instance!'
    assert value == 'FIZZ', 'Bad results for value'
    assert value2 == 'FIZZ', 'Bad results for value2'


def test_safe_func_on_dict_multi_index(test_dict, info_foo, info_bar, info_fizz):
    value = safe(test_dict) >> 'foo' >> [0, 1] >= 'info'
    value3 = safe(test_dict) >> 'foo' >> [] >= 'info'

    assert isinstance(value, tuple), f'The object must be a Sequence instance! Given: {type(value)}'
    assert value == (info_foo, info_bar,), 'Bad results'
    assert isinstance(value, tuple), f'The object must be a Sequence instance! Given: {type(value)}'
    assert value3 == (info_foo, info_bar, info_fizz,), 'Bad results'