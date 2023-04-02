from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class OrganizationId:
    value: str

    def __init__(self, value: str):
        assert value, "組織IDは必須です。"
        super().__setattr__("value", value)
