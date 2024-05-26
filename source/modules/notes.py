from source.modules.field import Field
from colorama import Fore, Style

class Note(Field):
    def __init__(self, note):
        if not self.is_note_valid(note):
            raise ValueError(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Note content exceeds 50 characters!")
        self.value = note

    def is_note_valid(self, note):
        return len(note) <= 50
    
    def add_tag(self, tags):
        for tag in tags:
            self.value += f" {tag}"
        return self.value