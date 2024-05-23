from datetime import datetime, timedelta
from collections import UserDict
from colorama import Fore, Style

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data: 
            raise Exception(f"{Fore.YELLOW}[Warning]{Style.RESET_ALL} {record.name.value} already in contact book")
        self.data[record.name.value] = record
    
    def find(self, name):
        record = self.data.get(name)
        return record

    def delete(self, name):
        del self.data[name]
        
    def __str__(self):
        lines = [str(record) for record in self.data.values()]
        return f"\n{Fore.GREEN}Here all your contacts{Style.RESET_ALL}: \n" + "".join(lines) 


    def get_upcoming_birthdays(self, days):
        current_date = datetime.today().date()
        list_of_upcoming_bdays = []
        contacts = self.data
        for name, record in contacts.items():
            user_obj = {}
            user_obj["name"] = name
            if(record.birthday != None):
                bday_obj = record.birthday.value.date()
                bday_day = bday_obj.day
                bday_month = bday_obj.month

                bday_this_year = datetime(
                year=current_date.year, month=bday_month, day=bday_day).date()
                
                diff = bday_this_year - current_date
                time_delta = timedelta(int(days))

                if (timedelta(int(0)) < diff <= time_delta):
                    list_of_upcoming_bdays.append(f"{name} has birthday on {bday_this_year.strftime('%d.%m.%Y')}")

        return list_of_upcoming_bdays

