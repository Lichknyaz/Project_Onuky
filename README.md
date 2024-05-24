# Project_Onuky

Bot will help your loved Granny to remember all information about family.

To start the bot, run `main.py` file.

### List of all functions:
- Add,change and delete contacts, phone numbers, emails, home address, birthdays of loved ones
- Calculate birthdays in the next days
- Add, change and delete notes
- Search for any saved data.
- Seach through the notes with any word or tags

### Used packages:
- colorama
- prompt-toolkit


### Basic syntax with examples:
- "hello"                                            to start using personal assistant;
- "exit"                                             to close the personal assistant;
- "add [name] [phone number]"                        to add contact;
- "change-phone [name] [old phone] [new phone]"      to change contact number;
- "all"                                              to get all contacts;
- "phone [name]"                                     to get contacts phone numbers;
- "delete-phone [name] [number]"                     to delete phone number";
- "add-birthday [name] [DD.MM.YYYY]"                 to add contacts birthday date";
- "show-birthday [name]"                             to show contacts birthday date;
- "birthdays [days]"                                 to show all birthdays for the following [days];
- "add-email [name] [email]"                         to add contacts email;
- "change-email [name] [email]"                      to change contacts email;
- "delete-email [name]"                              to delete contacts email;
- "delete-contact [name]"                            to delete contact from adress book fully;
- "add-address [name] [address in any format]"       to add home address;
- "change-adress [name] [new address in any format]" to change home address;
- "find [any word, digit or symbol]"                 to find all the matches in the contacts;
- "add-note [name] [note in any format]"             to add note to contact;
- "change-note [name] [new note in any format]"      to change note to contact;
- "delete-note [name]"                               to delete contacts note;
- "search-note [any word, digit or symbol]"          to search in contacts notes;
- "add-tags [name] [any word with # prefix]"         to tags to contacts notes;
