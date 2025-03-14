from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.key_binding import KeyBindings

class TriggeredCompleter(Completer):
    def __init__(self, trigger_char, options):
        self.trigger_char = trigger_char
        self.options = options

    def get_completions(self, document, complete_event):
        text_before = document.text_before_cursor
        if self.trigger_char not in text_before:
            return
            
        last_trigger_pos = text_before.rfind(self.trigger_char)
        current_segment = text_before[last_trigger_pos+1:].lstrip()
        original_segment = text_before[last_trigger_pos+1:]
        
        for option in self.options:
            if option.startswith(current_segment):
                start_pos = -len(original_segment)
                yield Completion(option, start_position=start_pos)

def advancde_input():
    # Define the trigger character and options
    trigger_char = "|"
    options = ["contains", "not contains", "matches"]
    
    # Create a completer instance
    completer = TriggeredCompleter(trigger_char, options)

    session = PromptSession(">", completer=completer, multiline=True)

    bindings = KeyBindings()
    # @bindings.add('enter')
    # def _(event):
    #     # Accept the current completion and insert a space
    #     event.app.current_buffer.insert_text(' ')
    #     event.app.current_buffer.complete_state = None
    @bindings.add('c-e')  # Ctrl+E to exit
    def _(event):
        event.app.exit()


    while True:
        try:
            text = session.prompt(key_bindings=bindings, multiline=True)
            print(f"You entered: {text}")
        except KeyboardInterrupt:
            break  # Control-C pressed
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
"""class CombinedCompleter(Completer):
    def __init__(self, completers):
        self.completers = completers

    def get_completions(self, document, complete_event):
        for completer in self.completers:
            yield from completer.get_completions(document, complete_event)

# Define multiple triggers
trigger1 = TriggeredCompleter("|", ["contains", "not contains", "matches"])
trigger2 = TriggeredCompleter("~", ["starts with", "ends with"])

# Combine them into a single completer
combined_completer = CombinedCompleter([trigger1, trigger2])

session = PromptSession("Enter query: ", completer=combined_completer)"""