from datetime import datetime
from field import Field

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Use DD.MM.YYYY format only")
        
    def __str__(self):
        return f"{self.value.strftime("%d.%m.%Y")}"