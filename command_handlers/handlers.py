import re
from command_handlers.input_error import input_error
from record import Record
from colorama import Fore, Style

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book) -> str:
    if len(args) != 2:
            return(f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"add {Fore.RED}[name]"{Fore.RESET}""")
    contact_name, phone = args
    contact = book.find(contact_name)
    message = (f"{Fore.GREEN}[Success]{Style.RESET_ALL} New phone added for {contact_name}")
    if not contact: 
        contact = Record(contact_name)
        book.add_record(contact)
        message = f"{Fore.GREEN}[Success]{Style.RESET_ALL} New contact added"
    if phone: 
        contact.add_phone(phone)
    return message


@input_error
def change_contact(args, book) -> str: 
    if len(args) != 3:
            return(f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"change {Fore.RED}[name] [old_n] [new_n]"{Fore.RESET}""")
    else:
        contact_name, old_phone, new_phone = args
        contact = book.find(contact_name)
        if contact is None: 
            return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
        else: 
            contact.edit_phone(old_phone, new_phone)
            return f"{Fore.GREEN}[Success]{Style.RESET_ALL} Contact updated"
        
@input_error
def remove_user_phone(args, book) -> str: 
    if len(args) != 2:
            return(f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"delete {Fore.RED}[name] [number]"{Fore.RESET}""")
    else:
        contact_name, phone = args
        contact = book.find(contact_name)
        if contact is None: 
            return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
        else: 
            contact.remove_phone(phone)
            return f"{Fore.GREEN}[Success]{Style.RESET_ALL} Phone number deleted"
        

@input_error
def show_phone(args, book) -> str:
    if len(args) != 1:
            return(f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"phone {Fore.RED}[name]"{Fore.RESET}""")
    contact_name = args[0]
    contact = book.find(contact_name)
    if contact is None: 
        return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
    else: 
        return contact

@input_error
def manage_birthday(args, book):
    if len(args) != 2:
        return f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"add-birthday {Fore.RED}[name] [DD.MM.YYYY]"{Fore.RESET}"""
    name, date = args
    contact = book.find(name)
    if contact is None: 
        return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
    else: 
        if contact.birthday:
            contact.manage_birthday(date)
            return f"{Fore.GREEN}[Success]{Style.RESET_ALL} Birthday updated"
        else:
            contact.manage_birthday(date)
            return f"{Fore.GREEN}[Success]{Style.RESET_ALL} Birthday added"

@input_error
def show_birthday(args, book):
    if len(args) != 1:
        return f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"show-birthday {Fore.RED}[name]"{Fore.RESET}"""
    name = args[0]
    contact = book.find(name)
    if contact is None: 
        return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
    else: 
        if contact.birthday:
            return contact.birthday
        else: 
            return f"{Fore.YELLOW}[Warining]{Style.RESET_ALL} Contact dont have birthday date"

@input_error
def add_user_email(args, book):
    if len(args) != 2: 
        return f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"add-email {Fore.RED}[name] [email]"{Fore.RESET}"""
    name, email = args 
    contact = book.find(name)
    if contact is None: 
        return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
    else: 
        contact.add_email(email)
        return f"{Fore.GREEN}[Success]{Style.RESET_ALL} Email added"
    
@input_error
def add_user_address(args, book):
    if len(args) < 2: 
        return f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"add-address {Fore.RED}[name] [adress]"{Fore.RESET}"""
    name, *address = args 
    contact = book.find(name)
    if contact is None: 
        return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
    else: 
        contact.add_address(address)
        return f"{Fore.GREEN}[Success]{Style.RESET_ALL} Address added"
    
@input_error
def change_user_address(args, book):
    if len(args) < 2: 
        return f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"change-adress {Fore.RED}[name] [adress]"{Fore.RESET}"""
    name, *address = args 
    contact = book.find(name)
    if contact is None: 
        return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
    else: 
        contact.add_address(address)
        return f"{Fore.GREEN}[Success]{Style.RESET_ALL} Address updated"
    
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
        return f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"change-email {Fore.RED}[name] [email]"{Fore.RESET}"""
    name, email = args 
    contact = book.find(name)
    if contact is None: 
        return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
    else: 
        contact.edit_email(email)
        return f"{Fore.GREEN}[Success]{Style.RESET_ALL} Email updated"
    
@input_error
def delete_user_email(args, book):
    if len(args) != 1: 
        return f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"delete-email {Fore.RED}[name]"{Fore.RESET}"""
    name = args[0]
    contact = book.find(name)
    if contact is None: 
        return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
    else: 
        contact.delete_email(name)
        return f"{Fore.GREEN}[Success]{Style.RESET_ALL} Email deleted"
    
@input_error
def remove_user_contact(args, book):
    if len(args) != 1: 
        return f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"remove-contact {Fore.RED}[name]"{Fore.RESET}"""
    name = args[0] 
    contact = book.find(name)
    if contact is None: 
        return f"{Fore.RED}[ERROR]{Style.RESET_ALL} Cant find contact"
    else: 
        book.delete(name)
        return f"{Fore.GREEN}[Success]{Style.RESET_ALL} Contact removed"

@input_error
def find(args, book):
    if len(args) != 1: 
        return f"""{Fore.RED}[ERROR]{Style.RESET_ALL} Wrong number of arguments
Try: {Fore.BLUE}"find {Fore.RED}[key]"{Fore.RESET} """
    
    search_item = args[0]
    contact_founded = False
    record = f"\n{Fore.GREEN}Here all search results{Style.RESET_ALL}: \n"

    for key, value in book.items():
        if search_item in f"{value}": 
            record += f"{book.find(key)}"
            contact_founded = True
    if not contact_founded:
        raise Exception(f"{Fore.YELLOW}[Warining]{Style.RESET_ALL} Cant find anything")

    return record

    
 