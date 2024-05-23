from libraries.name import Name
from libraries.phone import Phone
from libraries.birthday import Birthday
from libraries.user_email import Email
from libraries.address import Address
from libraries.notes import Note
from colorama import Fore, Style

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None
        self.note = None

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

        if self.note:
            contact_note = f", note: {self.note.value}"
            contact_full += contact_note

        return contact_full

    def add_phone(self, number: str): 
        for phone in self.phones: 
             if phone.value == number: 
                 raise Exception(f"{Fore.YELLOW}[Warning]{Style.RESET_ALL} Already in contact book")
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

    def add_note(self, note):
        self.note = Note(note)

    def edit_note(self, new_note):
        if not self.note:
            raise Exception(f"{Fore.RED}[ERROR]{Style.RESET_ALL} No note found.")
        if isinstance(new_note, list):
            self.note.add_tag(new_note)
        else:
            self.note = Note(new_note)

    def delete_note(self):
        if not self.note:
            raise Exception(f"{Fore.RED}[ERROR]{Style.RESET_ALL} No note found.")
        self.note = None

    def find_notes(self, query):
        found_notes = []
        if self.note:
            if query.lower() in self.note.value.lower():
                found_notes.append(self.note.value)
        return found_notes    