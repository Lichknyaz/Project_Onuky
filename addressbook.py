from datetime import datetime, timedelta
from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data: 
            raise KeyError(f"{record.name.value} already in contact book")
        self.data[record.name.value] = record
    
    def find(self, name):
        record = self.data.get(name)
        return record

    def delete(self, name):
        del self.data[name]

        
    def __str__(self):
        lines = [str(record) for record in self.data.values()]
        return "\n".join(lines)

    def upcoming_birthdays(self): 
        current_date = datetime.today().date()
        upcoming_birthdays = []
        message = ""

        for name, record in self.data.items():
            if record.birthday:
                user_birthday = datetime.strptime(str(record.birthday), "%d.%m.%Y").date().replace(year=current_date.year)

                days_before_birthday = (user_birthday - current_date).days
                if 0 <= days_before_birthday < 7: 
                    upcoming_birthdays.append(
                        {
                          f'name': name, 'congratulation_date': user_birthday.strftime('%d.%m.%Y')
                        }
                    )              
        for birthday in upcoming_birthdays:
            message += f"{birthday['name']}: {birthday['congratulation_date']} \n"
        
        return message

