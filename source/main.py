from source.command_handlers.handlers import *
from source.modules.storage import *
from source.modules.help_info import message, dict_of_commands
from source.modules import *
from source.modules.wordcompleter import FirstWordCompleter
from colorama import Fore, Style
from prompt_toolkit import prompt


def handler(command, book, *args):
        
        if command == "exit":
            print("Good bye, Granny!")
            save_data(book)
            exit()

        elif command == "help": 
            print(message)

        elif command == "hello":
            print("How can I help you, Granny?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "delete-phone":
            print(remove_user_phone(args, book))

        elif command == "change-phone": 
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all": 
            print(book)   

        elif command == "add-email":
            print(add_user_email(args, book))

        elif command == "change-email":
            print(change_user_email(args, book))

        elif command == "delete-email":
            print(delete_user_email(args, book))
        
        elif command == "add-birthday":
            print(manage_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "change-birthday":
            print(manage_birthday(args, book))

        elif command == "birthdays":
            print(upcoming_birthdays(args, book))
        
        elif command == "add-address":
            print(add_user_address(args,book))
        
        elif command == "change-address":
            print(change_user_address(args,book))
        
        elif command == "delete-contact":
            print(remove_user_contact(args, book))
        
        elif command == "find": 
            print(find(args, book))

        elif command == "add-note":
            print(add_note_to_contact(args, book))
    
        elif command == "change-note":
            print(edit_note_of_contact(args, book))
    
        elif command == "delete-note":
            print(delete_note_of_contact(args, book))   

        elif command == "search-note":
            print(search_notes(args, book))
        
        elif command == "add-tags":
            print(add_tag_to_note(args, book))  
            
        else:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid command. Please, use {Fore.BLUE}help{Style.RESET_ALL} if you forgot commands")


def main():
    book = load_data()
    print("Welcome to the assistant bot, Granny!\n", message)
    completer = FirstWordCompleter(dict_of_commands)
    while True:
        user_input = prompt("\nPlease, enter a command: ", completer=completer)
        command, *args = parse_input(user_input)
        handler(command, book, *args)



if __name__ == "__main__":
    main()
