import re
from command_handlers.input_error import input_error
from record import Record

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
def remove_user_phone(args, book) -> str: 
    if len(args) != 2:
            return("Wrong number of arguments")
    else:
        contact_name, phone = args
        contact = book.find(contact_name)
        if contact is None: 
            return "Cant find contact"
        else: 
            contact.remove_phone(phone)
            return "Phone number deleted"
        

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
def manage_birthday(args, book):
    if len(args) != 2:
        return "Wrong number of arguments"
    name, date = args
    contact = book.find(name)
    if contact is None: 
        return "Cant find contact"
    else: 
        if contact.birthday:
            contact.manage_birthday(date)
            return "Birthday updated"
        else:
            contact.manage_birthday(date)
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

@input_error
def add_user_email(args, book):
    if len(args) != 2: 
        return "Wrong number of arguments"
    name, email = args 
    contact = book.find(name)
    if contact is None: 
        return "Cant find contact"
    else: 
        contact.add_email(email)
        return "Email added"
    
@input_error
def add_user_address(args, book):
    if len(args) < 2: 
        return "Wrong number of arguments"
    name, *address = args 
    contact = book.find(name)
    if contact is None: 
        return "Cant find contact"
    else: 
        contact.add_address(address)
        return "Address added"
    
@input_error
def change_user_address(args, book):
    if len(args) < 2: 
        return "Wrong number of arguments"
    name, *address = args 
    contact = book.find(name)
    if contact is None: 
        return "Cant find contact"
    else: 
        contact.add_address(address)
        return "Address updated"
    
@input_error
def upcoming_birthdays(args, book):
    days, *_ = args
    upcoming_bdays = book.get_upcoming_birthdays(days)
    str_ = ''
    for bday in upcoming_bdays:
        str_ += f"{bday}; "
    return str_

@input_error
def change_user_email(args, book):
    if len(args) != 2: 
        return "Wrong number of arguments"
    name, email = args 
    contact = book.find(name)
    if contact is None: 
        return "Cant find contact"
    else: 
        contact.edit_email(email)
        return "Email updated"
    
@input_error
def delete_user_email(args, book):
    if len(args) != 1: 
        return "Wrong number of arguments"
    name = args[0]
    contact = book.find(name)
    if contact is None: 
        return "Cant find contact"
    else: 
        contact.delete_email(name)
        return "Email deleted"
    
@input_error
def remove_user_contact(args, book):
    if len(args) != 1: 
        return "Wrong number of arguments"
    name = args[0] 
    contact = book.find(name)
    if contact is None: 
        return "Cant find contact"
    else: 
        book.delete(name)
        return "Contact removed"

@input_error
def find(args, book):
    if len(args) != 1: 
        return "Wrong number of arguments"
    
    search_item = args[0]
    contact_founded = False
    record = ""

    for key, value in book.items():
        if search_item in f"{value}": 
            record += f"\n {book.find(key)} \n"
            contact_founded = True
    if not contact_founded:
        raise Exception("Cant find anything")

    return record

    
 