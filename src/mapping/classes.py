from __future__ import annotations
from typing import Any


class SafeDict(dict):
    """Class for safe key access"""
    
    def __rshift__(self, key: str) -> SafeDict | Any:
        value = self.get(key)
        if isinstance(value, dict):
            return SafeDict(**value)
        return value
    
    def __ge__(self, value):
        return value