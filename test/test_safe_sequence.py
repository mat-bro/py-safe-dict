from ..src import SafeSequence


def test_get_simple_attribute(test_list_base):
    value = SafeSequence(test_list_base) >> [2] >> 'category'
    value2 = SafeSequence(test_list_base) >> [2] >= 'category'

    assert isinstance(value, str), f'The object must be a str instance!'
    assert isinstance(value2, str), f'The object must be a str instance!'
    assert value == 'FIZZ', 'Bad results for value'
    assert value2 == 'FIZZ', 'Bad results for value2'


def test_get_all_sequence_attributes(test_list_base):
    value = SafeSequence(test_list_base) >> [] >> 'category'
    value2 = SafeSequence(test_list_base) >> [] >= 'category'

    assert isinstance(value, tuple), f'The object must be a tuple instance!'
    assert isinstance(value2, tuple), f'The object must be a tuple instance!'
    assert value == ('FOO', 'BAR', 'FIZZ'), 'Bad results for value'
    assert value2 == ('FOO', 'BAR', 'FIZZ'), 'Bad results for value2'


def test_get_all_sequence_attributes_with_range(test_list_base):
    value = SafeSequence(test_list_base) >> range(0, 2) >> 'category'
    value2 = SafeSequence(test_list_base) >> range(0, 2) >= 'category'

    assert isinstance(value, tuple), f'The object must be a tuple instance!'
    assert isinstance(value2, tuple), f'The object must be a tuple instance!'
    assert value == ('FOO', 'BAR',), 'Bad results for value'
    assert value2 == ('FOO', 'BAR',), 'Bad results for value2'