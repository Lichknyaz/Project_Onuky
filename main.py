from command_handlers.handlers import *
from storage import *
from colorama import Fore, Style

hello_commands = ["hello", "hi"]
close_commands = ["close", "exit", "leave", "bye"]
add_command = ["add"]
change_command = ["change"]
get_all_contacts_command = ["all"]
get_contact_command = ["phone"]
remove_phone = ["delete"]
add_user_birthday = ["add-birthday"]
get_user_birthday = ["show-birthday"]
change_user_birthday = ["change-birthday"]
birthdays = ["birthdays"]
add_email = ["add-email"]
add_address = ["add-address"]
change_address = ["change-address"]
change_email = ["change-email"]
remove_email = ["delete-email"]
remove_contact = ['remove-contact']
find_command = ['find']

massage = f"""\n You can use this commands: \n
{Fore.BLUE}"hi"                              {Fore.RESET} to start using personal assistant;
{Fore.BLUE}"close\\exit\\leave\\bye"            {Fore.RESET} to close the personal assistant;
{Fore.BLUE}"add {Fore.RED}[name]"                      {Fore.RESET} to add contact;
{Fore.BLUE}"change {Fore.RED}[name] [old_n] [new_n]"   {Fore.RESET} to change contact number; 
{Fore.BLUE}"all"                             {Fore.RESET} to get all contacts; 
{Fore.BLUE}"phone {Fore.RED}[name]"                    {Fore.RESET} to get full contact; 
{Fore.BLUE}"delete {Fore.RED}[name] [number]"          {Fore.RESET} to delete phone number";
{Fore.BLUE}"add-birthday {Fore.RED}[name] [DD.MM.YYYY]"{Fore.RESET} to add user birthday date";
{Fore.BLUE}"show-birthday {Fore.RED}[name]"            {Fore.RESET} to show user birthday date;
{Fore.BLUE}"birthdays {Fore.RED}[days]"                {Fore.RESET} to show all birthdays for the following [days];
{Fore.BLUE}"add-email {Fore.RED}[name] [email]"        {Fore.RESET} to add user email;
{Fore.BLUE}"change-email {Fore.RED}[name] [email]"     {Fore.RESET} to change user email; 
{Fore.BLUE}"delete-email {Fore.RED}[name]"             {Fore.RESET} to delete user email;
{Fore.BLUE}"remove-contact {Fore.RED}[name]"           {Fore.RESET} to delete contact from adress book fully; 
{Fore.BLUE}"add-address {Fore.RED}[name] [adress]"     {Fore.RESET} to find all the matches in the contacts; 
{Fore.BLUE}"change-adress {Fore.RED}[name] [adress]"   {Fore.RESET} to find all the matches in the contacts;
{Fore.BLUE}"find {Fore.RED}[key]"                      {Fore.RESET} to find all the matches in the contacts;
          """


def handler(command, book, *args):
        
        if command in close_commands:
            print("Good bye!")
            save_data(book)
            exit()

        elif command in "help": 
            print(massage)

        elif command in hello_commands:
            print("How can I help you?")

        elif command in add_command:
            print(add_contact(args, book))

        elif command in remove_phone:
            print(remove_user_phone(args, book))

        elif command in change_command: 
            print(change_contact(args, book))

        elif command in get_contact_command:
            print(show_phone(args, book))

        elif command in get_all_contacts_command: 
            print(book)   

        elif command in add_email:
            print(add_user_email(args, book))

        elif command in change_email:
            print(change_user_email(args, book))

        elif command in remove_email:
            print(delete_user_email(args, book))
        
        elif command in add_user_birthday:
            print(manage_birthday(args, book))

        elif command in get_user_birthday:
            print(show_birthday(args, book))

        elif command in change_user_birthday:
            print(manage_birthday(args, book))

        elif command in birthdays:
            print(upcoming_birthdays(args, book))
        
        elif command in add_address:
            print(add_user_address(args,book))
        
        elif command in change_address:
            print(change_user_address(args,book))
        
        elif command in remove_contact:
            print(remove_user_contact(args, book))
        
        elif command in find_command: 
            print(find(args, book))

        else:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid command. Use {Fore.BLUE}help{Style.RESET_ALL} if you forgot commands")


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("\nEnter a command: ")
        command, *args = parse_input(user_input)
        handler(command, book, *args)



if __name__ == "__main__":
    main()
 


