from __future__ import annotations
from collections.abc import Sequence
from abc import ABC, abstractmethod
from typing import Any

# TODO: extend for all Mapping and Sequence

def _get_instance(value):
    if isinstance(value, Sequence)\
        and not isinstance(value, str):
        return SafeSequence(value)
    elif isinstance(value, dict):
        return SafeDict(**value)
    elif value is None or isinstance(value, SafeNone):
        return SafeNone()
    return value


class SafeObject(ABC):

    @abstractmethod
    def __rshift__(self):
        pass


    @abstractmethod
    def __ge__(self):
        pass
    


class SafeDict(dict, SafeObject):
    """Class for safe key access"""

    def __rshift__(self, key: str) -> SafeDict | Any:
        value = self.get(key)
        return _get_instance(value)
    

    def __ge__(self, key: str) -> Any:
        return self.get(key)
    


class SafeSequence(tuple, SafeObject):

    def __rshift__(self, value: list[int]) -> SafeSequence | Any:
        seq_len = len(value)

        if seq_len:
            if seq_len == 1:
                return _get_instance(
                    self.__getitem__(*value)
                    )
            return SafeMultiSequence(
                _get_instance(val) for val in map(self.__getitem__, value)
                )
        return SafeMultiSequence(
            _get_instance(val) for val in map(self.__getitem__, range(len(self)))
            )
    
    
    def __ge__(self, value: list[int]) -> Any:
        index = value[0]
        return self.__getitem__(index)

   

class SafeMultiSequence(SafeSequence, SafeObject):    
    def __rshift__(self, value: str | list[int]) -> SafeSequence | Any:
        if isinstance(value, str):
            return SafeMultiSequence(val.get(value) for val in self)
        
    
    def __ge__(self, value: str | list[int]) -> Any:
        if isinstance(value, str):
            return tuple(val.get(value) for val in self)


class SafeNone(SafeObject):
    __slots__ = ()

    def __rshift__(self, _: str | list[int]) -> SafeNone | None:
        return SafeNone()
    
    def __ge__(self, _: str | list[int]) -> None:
        """This method returns None"""

    def __str__(self):
        """This method returns None"""