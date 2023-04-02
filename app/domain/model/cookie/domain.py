from __future__ import annotations

from dataclasses import dataclass
from typing import Set

import tldextract as tldextract
from tldextract.tldextract import ExtractResult

from domain.model.url import URL


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Domain:
    value: str

    def __init__(self, value: str):
        assert value, 'ドメイン名は必須です。'
        super().__setattr__('value', value)

    @staticmethod
    def domains_of(url: URL) -> Set[Domain]:
        extract_result: ExtractResult = tldextract.extract(url.value)
        return {
            Domain(f'.{extract_result.domain}.{extract_result.suffix}'),
            Domain(f'.{extract_result.subdomain}.{extract_result.domain}.{extract_result.suffix}'),
            Domain(f'{extract_result.subdomain}.{extract_result.domain}.{extract_result.suffix}'),
        }
