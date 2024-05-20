import re
from command_handlers.input_error import input_error
from record import Record
from addressbook import AddressBook

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book) -> str:
    contact_name, phone = args
    contact = book.find(contact_name)
    message = (f"New phone added for {contact_name}")
    if not contact: 
        contact = Record(contact_name)
        book.add_record(contact)
        message = "New contact added"
    if phone: 
        contact.add_phone(phone)
    return message


@input_error
def change_contact(args, book) -> str: 
    if len(args) != 3:
            return("Wrong number of arguments")
    else:
        contact_name, old_phone, new_phone = args
        contact = book.find(contact_name)
        if contact is None: 
            return "Cant find contact"
        else: 
            contact.edit_phone(old_phone, new_phone)
            return "Contact updated"
        
@input_error
def remove_contact(args, book) -> str: 
    if len(args) != 2:
            return("Wrong number of arguments")
    else:
        contact_name, phone = args
        contact = book.find(contact_name)
        if contact is None: 
            return "Cant find contact"
        else: 
            contact.remove_phone(phone)
            return "Contact deleted"
        

@input_error
def show_phone(args, book) -> str:
    if len(args) != 1:
            return("Wrong number of arguments")
    contact_name = args[0]
    contact = book.find(contact_name)
    if contact is None: 
        return "Cant find contact"
    else: 
        return contact

@input_error
def add_birthday(args, book):
    if len(args) != 2:
        return "Wrong number of arguments"
    name, date = args
    contact = book.find(name)
    if contact is None: 
        return "Cant find contact"
    else: 
        contact.add_birthday(date)
        return "Birthday added"


@input_error
def show_birthday(args, book):
    if len(args) != 1:
        return "Wrong number of arguments"
    name = args[0]
    contact = book.find(name)
    if contact is None: 
        return "Cant find contact"
    else: 
        if contact.birthday:
            return contact.birthday
        else: 
            return "Contact dont have birthday date"





