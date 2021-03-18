# stdlib
from typing import Any
from typing import Dict
from typing import List


class Protocol(type):
    registered_protocols: Dict[Any, Any] = {}

    def __new__(cls, name: str, bases, dct: Dict[Any, Any]):
        new_cls = super().__new__(cls, name, bases, dct)
        Protocol.registered_protocols[name] = new_cls

        def __init__(self, *args: List[Any], **kwargs: Dict[Any, Any]) -> None:  # noqa
            raise ValueError("Protocol class should not be instantiated")

        setattr(new_cls, "__init__", __init__)
        return new_cls