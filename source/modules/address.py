from source.modules.field import Field

class Address(Field):
    def __init__(self, address: list):
        self.value = " ".join(address)