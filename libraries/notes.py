from libraries.field import Field

class Note(Field):
    def __init__(self, note):
        if not self.is_note_valid(note):
            raise ValueError("Note content exceeds 50 characters!")
        self.value = note

    def is_note_valid(self, note):
        return len(note) <= 50