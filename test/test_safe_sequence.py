from ..src import SafeSequence


def test_get_simple_attribute(test_list_base):
    value = SafeSequence(test_list_base) >> [2] >> 'info' >> 'name'
    value2 = SafeSequence(test_list_base) >> [2] >> 'info' >= 'name'

    assert isinstance(value, str), f'The object must be a str instance!'
    assert isinstance(value2, str), f'The object must be a str instance!'
    assert value == 'FIZZ', 'Bad results for value'
    assert value2 == 'FIZZ', 'Bad results for value2'