from name import Name
from phone import Phone
from birthday import Birthday
from command_handlers.input_error import input_error

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        contact_full = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

        if self.birthday: 
            contact_birthday = f", Birthday date: {self.birthday}"
            contact_full += contact_birthday

        return contact_full

    def add_phone(self, number: str): 
        for phone in self.phones: 
             if phone.value == number: 
                 raise KeyError(f"{phone.value} already in contact book")
        else:
            self.phones.append(Phone(number))

    def remove_phone(self, number: int): 
        for phone in self.phones: 
            if phone.value == number:
                self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        contact_founded = False

        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                contact_founded = True
                break
        if not contact_founded:
            raise Exception("Cant find contact phone")
            

    def find_phone(self, number): 
        for phone in self.phones: 
            if phone.value == number: 
                return phone
            
    def add_birthday(self, date): 
        self.birthday = Birthday(date)
 