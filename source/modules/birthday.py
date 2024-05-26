from datetime import datetime
from source.modules.field import Field
from colorama import Fore, Style

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError(f"{Fore.YELLOW}[Warning]{Style.RESET_ALL} Use DD.MM.YYYY format only")
        
    def __str__(self):
        return f"{self.value.strftime('%d.%m.%Y')}"