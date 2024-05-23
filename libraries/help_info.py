from colorama import Fore, Style

message = f"""\nYou can use this commands: \n
{Fore.BLUE}"hello"                                         {Fore.RESET} to start using personal assistant;
{Fore.BLUE}"exit"                                          {Fore.RESET} to close the personal assistant;
{Fore.BLUE}"add {Fore.RED}[name] [phone number]"                     {Fore.RESET} to add contact;
{Fore.BLUE}"change-phone {Fore.RED}[name] [old phone] [new phone]"   {Fore.RESET} to change contact number; 
{Fore.BLUE}"all"                                           {Fore.RESET} to get all contacts; 
{Fore.BLUE}"phone {Fore.RED}[name]"                                  {Fore.RESET} to get full contact; 
{Fore.BLUE}"delete-phone {Fore.RED}[name] [number]"                  {Fore.RESET} to delete phone number";
{Fore.BLUE}"add-birthday {Fore.RED}[name] [DD.MM.YYYY]"              {Fore.RESET} to add contacts birthday date";
{Fore.BLUE}"show-birthday {Fore.RED}[name]"                          {Fore.RESET} to show contacts birthday date;
{Fore.BLUE}"birthdays {Fore.RED}[days]"                              {Fore.RESET} to show all birthdays for the following [days];
{Fore.BLUE}"add-email {Fore.RED}[name] [email]"                      {Fore.RESET} to add contacts email;
{Fore.BLUE}"change-email {Fore.RED}[name] [email]"                   {Fore.RESET} to change contacts email; 
{Fore.BLUE}"delete-email {Fore.RED}[name]"                           {Fore.RESET} to delete contacts email;
{Fore.BLUE}"delete-contact {Fore.RED}[name]"                         {Fore.RESET} to delete contact from adress book fully; 
{Fore.BLUE}"add-address {Fore.RED}[name] [adress]"                   {Fore.RESET} to add home address; 
{Fore.BLUE}"change-adress {Fore.RED}[name] [adress]"                 {Fore.RESET} to change home address;
{Fore.BLUE}"find {Fore.RED}[key]"                                    {Fore.RESET} to find all the matches in the contacts;
{Fore.BLUE}"add-note {Fore.RED}[name] [note]"                        {Fore.RESET} to add note to contact;
{Fore.BLUE}"change-note {Fore.RED}[name] [new note]"                 {Fore.RESET} to change note to contact;
{Fore.BLUE}"delete-note {Fore.RED}[name]"                            {Fore.RESET} to delete contacts note;
          """

dict_of_commands = {
                    "hello": "Greetings",
                    "exit": "Closing the bot",
                    "add": "Adding contact - Enter [name [10-digit phone number]",
                    "all": "Shows all contacts",
                    "change-phone": "Changing phone number - Enter [name] [old number] [new number]",
                    "phone": "Show contacts phone - Enter [name]",
                    "delete-phone": "Delete contacts phone - Enter [name] [phone number]",
                    "add-birthday": "Adding contacts birthday - Enter [name] [DD.MM.YYYY]",
                    "show-birthday": "Show contacts birthday - Enter [name]",
                    "birthdays": "Shows all birthdays in next defined days - Enter [days]",
                    "add-email": "Adding contacts email - Enter [name] [email]",
                    "change-email": "Changing contacts email - Enter [name] [new_email]",
                    "delete-email": "Adding contacts email - Enter [name] [email]",
                    "delete-contact": "Delete contact - Enter [name]",
                    "find": "Find contact with any key - Enter [any key]",
                    "add-address": "Adding contacts home address - Enter [name] [address in any format]",
                    "change-address": "Changing contacts home address - Enter [name] [address in any format]",
                    "add-note": "Adding note to contact - Enter [name] [note in any format]",
                    "change-note": "Changing contacts note - Enter [name] [note in any format]",
                    "delete-note": "Delete contacts note - Enter [name]",
                    "add-tags": "Adding tags to note - Enter [name] [any word with # prefix]"
                  }
