from dataclasses import dataclass

from domain.model.page.html import CharacterCode


@dataclass(init=False, unsafe_hash=True, frozen=True)
class HTML:
    text: str
    character_code: CharacterCode

    def __init__(self, text: str, character_code: CharacterCode):
        super().__setattr__("text", text)
        super().__setattr__("character_code", character_code)

    def is_not_empty(self) -> bool:
        return self.text is not None and self.text != ''
