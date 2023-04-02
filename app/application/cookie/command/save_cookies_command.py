from dataclasses import dataclass
from typing import Set


@dataclass(init=True, unsafe_hash=True, frozen=True)
class SaveCookiesCommand:
    @dataclass(init=True, unsafe_hash=True, frozen=True)
    class Cookie:
        domain: str
        path: str
        name: str
        value: str

    organization_id: str
    cookies: Set[Cookie]
