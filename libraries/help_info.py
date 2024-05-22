from colorama import Fore, Style

message = f"""\nYou can use this commands: \n
{Fore.BLUE}"hello"                                        {Fore.RESET} to start using personal assistant;
{Fore.BLUE}"exit"                                         {Fore.RESET} to close the personal assistant;
{Fore.BLUE}"add {Fore.RED}[name] [phone number]"                    {Fore.RESET} to add contact;
{Fore.BLUE}"change-phone {Fore.RED}[name] [old phone] [new phone]"  {Fore.RESET} to change contact number; 
{Fore.BLUE}"all"                                          {Fore.RESET} to get all contacts; 
{Fore.BLUE}"phone {Fore.RED}[name]"                                 {Fore.RESET} to get full contact; 
{Fore.BLUE}"delete-phone {Fore.RED}[name] [number]"                 {Fore.RESET} to delete phone number";
{Fore.BLUE}"add-birthday {Fore.RED}[name] [DD.MM.YYYY]"             {Fore.RESET} to add contacts birthday date";
{Fore.BLUE}"show-birthday {Fore.RED}[name]"                         {Fore.RESET} to show contacts birthday date;
{Fore.BLUE}"birthdays {Fore.RED}[days]"                             {Fore.RESET} to show all birthdays for the following [days];
{Fore.BLUE}"add-email {Fore.RED}[name] [email]"                     {Fore.RESET} to add contacts email;
{Fore.BLUE}"change-email {Fore.RED}[name] [email]"                  {Fore.RESET} to change contacts email; 
{Fore.BLUE}"delete-email {Fore.RED}[name]"                          {Fore.RESET} to delete contacts email;
{Fore.BLUE}"delete-contact {Fore.RED}[name]"                        {Fore.RESET} to delete contact from adress book fully; 
{Fore.BLUE}"add-address {Fore.RED}[name] [adress]"                  {Fore.RESET} to add home address; 
{Fore.BLUE}"change-adress {Fore.RED}[name] [adress]"                {Fore.RESET} to change home address;
{Fore.BLUE}"find {Fore.RED}[key]"                                   {Fore.RESET} to find all the matches in the contacts;
{Fore.BLUE}"add-note {Fore.RED}[name] [note]"                       {Fore.RESET} to add note to contact;
{Fore.BLUE}"change-note {Fore.RED}[name] [new note]"                {Fore.RESET} to change note to contact;
{Fore.BLUE}"delete-note {Fore.RED}[name]"                           {Fore.RESET} to delete contacts note;
          """