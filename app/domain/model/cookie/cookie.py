from dataclasses import dataclass

from domain.model.cookie import Domain, Path


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Cookie:
    domain: Domain
    path: Path
    name: str
    value: str

    def __init__(self, domain: Domain, path: Path, name: str, value: str):
        assert domain, 'ドメイン名は必須です。'
        assert path, 'パスは必須です。'
        assert name, 'クッキー名は必須です。'
        assert isinstance(value, str), 'クッキーのコンテンツには文字列を指定してください。'
        super().__setattr__('domain', domain)
        super().__setattr__('path', path)
        super().__setattr__('name', name)
        super().__setattr__('value', value)
