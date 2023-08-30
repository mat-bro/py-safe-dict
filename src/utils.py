from __future__ import annotations
from typing import Any

from .classes import SafeDict, SafeSequence, _get_instance, SafeObject


def safe(obj: Any) -> SafeDict | SafeSequence:
    value = _get_instance(obj)
    if isinstance(value, SafeObject):
        return value
    else:
        NotImplementedError(
            f"Object of type={type(obj)} can't be secured!"
        )
