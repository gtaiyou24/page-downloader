from __future__ import annotations

from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Path:
    value: str

    def __init__(self, value: str):
        assert value, 'パスは必須です。'
        super().__setattr__('value', value)
