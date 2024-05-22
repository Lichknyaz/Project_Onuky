from command_handlers.handlers import *
from storage import *
from colorama import Fore, Style
from help_info import massage
from prompt_toolkit import prompt
from wordcompleter import FirstWordCompleter

hello_commands = ["hello"]
close_commands = ["exit"]
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
remove_contact = ["remove-contact"]
find_command = ["find"]
add_note_command = ["add-note"]
edit_note_command = ["edit-note"]
delete_note_command = ["delete-note"]


dict_of_commands = {
                    "hello": "Greetings",
                    "exit": "Closing the bot",
                    "add": "Adding contact - Enter [name [10-digit phone number]",
                    "all": "Shows all contacts",
                    "change": "Changing phone number - Enter [name] [old number] [new number]",
                    "phone": "Show contacts phone - Enter [name]",
                    "delete": "Delete contacts phone - Enter [name] [phone number]",
                    "add-birthday": "Adding contacts birthday - Enter [name] [DD.MM.YYYY]",
                    "show-birthday": "Show contacts birthday - Enter [name]",
                    "birthdays": "Shows all birthdays in next defined days - Enter [days]",
                    "add-email": "Adding contacts email - Enter [name] [email]",
                    "change-email": "Changing contacts email - Enter [name] [new_email]",
                    "delete-email": "Adding contacts email - Enter [name] [email]",
                    "remove-contact": "Delete contact - Enter [name]",
                    "find": "Find contact with any key - Enter [any key]",
                    "add-address": "Adding contacts home address - Enter [name] [address in any format]",
                    "change-address": "Changing contacts home address - Enter [name] [address in any format]",
                    "add-note": "Adding note to contact - Enter [name] [note in any format]",
                    "edit-note": "Changing contacts note - Enter [name] [note in any format]",
                    "delete-note": "Delete contacts note - Enter [name]",
                    }




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

        elif command in add_note_command:
            print(add_note_to_contact(args, book))
    
        elif command in edit_note_command:
            print(edit_note_of_contact(args, book))
    
        elif command in delete_note_command:
            print(delete_note_of_contact(args, book))    

        else:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid command. Use {Fore.BLUE}help{Style.RESET_ALL} if you forgot commands")


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    completer = FirstWordCompleter(dict_of_commands)
    while True:
        user_input = prompt("\nEnter a command: ", completer=completer)
        command, *args = parse_input(user_input)
        handler(command, book, *args)



if __name__ == "__main__":
    main()
