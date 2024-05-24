from prompt_toolkit.completion import Completer, Completion

class FirstWordCompleter(Completer):
    def __init__(self, commands):
        self.commands = commands

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        if ' ' in text:
            return
        for command, description in self.commands.items():
            if command.startswith(text):
                yield Completion(command, start_position=-len(text), display=f'{command} - {description}')