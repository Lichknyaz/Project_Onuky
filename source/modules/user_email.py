from source.modules.field import Field
import re
from colorama import Fore, Style

class Email(Field):
    def __init__(self, email):
        self.value = self.validate(email)

    def validate(self, email): 
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if not (re.fullmatch(regex, email)):
            raise ValueError(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Worng format of email, please try again.")
        else:
            return email