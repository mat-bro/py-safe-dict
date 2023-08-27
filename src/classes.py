from __future__ import annotations
# from collections.abc import Sequence
from typing import Any

# TODO: extend for all Mapping and Sequence

def _get_instance(value):
    if isinstance(value, (list, tuple)):
        return SafeSequence(value)
    elif isinstance(value, dict):
        return SafeDict(**value)
    elif value is None or isinstance(value, SafeNone):
        return SafeNone()
    return value


class SafeDict(dict):
    """Class for safe key access"""

    def __rshift__(self, key: str) -> SafeDict | Any:
        value = self.get(key)
        return _get_instance(value)
    
    def __ge__(self, key: str) -> Any:
        return self.get(key)
    


class SafeSequence(tuple):
    def __rshift__(self, value: list[int]) -> SafeSequence | Any:
        index = value[0]
        value = self.__getitem__(index)
        return _get_instance(value)
    
    def __ge__(self, value: list[int]) -> Any:
        index = value[0]
        return self.__getitem__(index)

    

class SafeNone:
    def __rshift__(self, _: str | list[int]) -> SafeNone | None:
        return SafeNone()
    
    def __ge__(self, _: str | list[int]) -> None:
        """This method returns None"""

    def __str__(self):
        """This method returns None"""