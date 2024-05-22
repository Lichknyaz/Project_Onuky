from colorama import Fore, Style

massage = f"""\nYou can use this commands: \n
{Fore.BLUE}"hi"                              {Fore.RESET} to start using personal assistant;
{Fore.BLUE}"close\\exit\\leave\\bye"            {Fore.RESET} to close the personal assistant;
{Fore.BLUE}"add {Fore.RED}[name] [number]"                      {Fore.RESET} to add contact;
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