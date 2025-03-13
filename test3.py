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

def main():
    # Define the trigger character and options
    trigger_char = "|"
    options = ["contains", "not contains", "matches"]
    
    # Create a completer instance
    completer = TriggeredCompleter(trigger_char, options)

    session = PromptSession("Enter query (multiline): ", multiline=True, completer=completer)

    bindings = KeyBindings()
    
    # This binding is not necessary if you want to keep the default Enter behavior.
    # It's added here to show how you might customize Enter, but it's commented out.
    # @bindings.add('enter')
    # def _(event):
    #     # This would override the default Enter behavior, so it's commented out.
    #     pass

    # Use Meta+Enter to submit the input
    # The default behavior for Meta+Enter is already set by prompt_toolkit.

    # Optionally, add a custom key binding to exit or perform another action.
    @bindings.add('c-e')  # Ctrl+E to exit
    def _(event):
        event.app.exit()

    session.key_bindings = bindings

    while True:
        try:
            text = session.prompt()
            print(f"You entered: {text}")
        except KeyboardInterrupt:
            break  # Control-C pressed
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
