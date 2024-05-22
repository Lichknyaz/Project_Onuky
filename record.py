from name import Name
from phone import Phone
from birthday import Birthday
from user_email import Email
from notes import Note

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.note = None

    def __str__(self):
        contact_full = f"Contact name: {self.name.value}"

        if len(self.phones) != 0: 
            phones = f", phones: {'; '.join(p.value for p in self.phones)}"
            contact_full += phones

        if self.birthday: 
            contact_birthday = f", Birthday date: {self.birthday}"
            contact_full += contact_birthday

        if self.email: 
            email = f", email: {self.email.value}"
            contact_full += email

        if self.note:
            contact_note = f", note: {self.note.value}"
            contact_full += contact_note

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

    def add_email(self, email): 
        self.email = Email(email)

    def add_note(self, note):
        """ Добавляємо нотатки """
        if len(note) > 100:
            raise ValueError("Note content exceeds 100 characters.")
        self.note = Note(note)

    def edit_note(self, new_note):
        """ Редагуємо нотатки """
        if not self.note:
            raise KeyError("No note found.")
        if len(new_note) > 50:
            raise ValueError("Note content exceeds 50 characters.")
        self.note = Note(new_note)

    def delete_note(self):
        """ Видаляємо нотатки """
        if not self.note:
            raise KeyError("No note found.")
        self.note = None 