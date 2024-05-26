from source.modules.field import Field
from colorama import Fore, Style

class Phone(Field):
    def __init__(self, number):
        self.value = self.validate(number)

    def validate(self, number): 
            
        if not number.isdigit(): 
            raise ValueError(f"{Fore.YELLOW}[Warning]{Style.RESET_ALL} Only digits")
            
        if len(number) != 10: 
            raise ValueError(f"{Fore.YELLOW}[Warning]{Style.RESET_ALL} Phone number must have 10 digits")
              
        return number