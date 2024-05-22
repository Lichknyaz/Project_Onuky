from name import Name
from phone import Phone
from birthday import Birthday
from user_email import Email
from address import Address
from colorama import Fore, Style

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def __str__(self):
        contact_full = f"\nContact name: {self.name.value}"

        if len(self.phones) != 0: 
            phones = f", phones: {'; '.join(p.value for p in self.phones)}"
            contact_full += phones

        if self.birthday: 
            contact_birthday = f", Birthday date: {self.birthday}"
            contact_full += contact_birthday

        if self.email: 
            email = f", email: {self.email.value}"
            contact_full += email
        
        if self.address:
            address = f", address: {self.address.value}"
            contact_full += address

        return contact_full

    def add_phone(self, number: str): 
        for phone in self.phones: 
             if phone.value == number: 
                 raise Exception(f"{Fore.YELLOW}[Warning]{Style.RESET_ALL} already in contact book")
        else:
            self.phones.append(Phone(number))

    def remove_phone(self, number: int): 
        contact_founded = False
        for phone in self.phones: 
            if phone.value == number:
                self.phones.remove(phone)
                contact_founded = True
                break
        if not contact_founded:
            raise Exception(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact phone")

    def edit_phone(self, old_phone, new_phone):
        contact_founded = False

        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                contact_founded = True
                break
        if not contact_founded:
            raise Exception(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact phone")
            

    def find_phone(self, number): 
        for phone in self.phones: 
            if phone.value == number: 
                return phone
            
    def manage_birthday(self, date): 
        self.birthday = Birthday(date)

    def add_email(self, email): 
        self.email = Email(email)

    def edit_email(self, email):
        self.email = Email(email) 

    def delete_email(self, name):
           self.email = None 

    def add_address(self, address):
        self.address = Address(address)