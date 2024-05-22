from command_handlers.handlers import *
from storage import *

hello_commands = ["hello", "hi"]
close_commands = ["close", "exit", "leave", "bye"]
add_command = ["add"]
change_command = ["change"]
get_all_contacts_command = ["all"]
get_contact_command = ["phone"]
delete_command = ["delete"]
add_user_birthday = ["add-birthday"]
get_user_birthday = ["show-birthday"]
birthdays = ["birthdays"]
add_email = ["add-email"]
add_note_command = ["add-note"]
edit_note_command = ["edit-note"]
delete_note_command = ["delete-note"]




def handler(command, book, *args):
        
        if command in close_commands:
            print("Good bye!")
            save_data(book)
            exit()
        elif command in hello_commands:
            print("How can I help you?")

        elif command in add_command:
            print(add_contact(args, book))

        elif command in delete_command:
            print(remove_contact(args, book))

        elif command in change_command: 
            print(change_contact(args, book))

        elif command in get_contact_command:
            print(show_phone(args, book))

        elif command in get_all_contacts_command: 
            print(book)   

        elif command in add_email:
            print(add_user_email(args, book))
        
        elif command in add_user_birthday:
            print(add_birthday(args, book))

        elif command in get_user_birthday:
            print(show_birthday(args, book))

        elif command in birthdays:
            print(upcoming_birthdays(args, book))

        elif command in add_note_command:
            print(add_note_to_contact(args, book))
    
        elif command in edit_note_command:
            print(edit_note_of_contact(args, book))
    
        elif command in delete_note_command:
            print(delete_note_of_contact(args, book))    

        else:
            print("Invalid command.")


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        handler(command, book, *args)



if __name__ == "__main__":
    main()
