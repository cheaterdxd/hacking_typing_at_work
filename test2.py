from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.key_binding import KeyBindings

class PipeTriggeredCompleter(Completer):
    def get_completions(self, document, complete_event):
        text_before = document.text_before_cursor
        if "|" not in text_before:
            return
            
        last_pipe_pos = text_before.rfind("|")
        current_segment = text_before[last_pipe_pos+1:].lstrip()
        original_segment = text_before[last_pipe_pos+1:]
        
        for option in ["contains", "not contains", "matches"]:
            if option.startswith(current_segment):
                start_pos = -len(original_segment)
                yield Completion(option, start_position=start_pos)

def main():
    session = PromptSession("Enter query: ", completer=PipeTriggeredCompleter(), multiline=True)

    bindings = KeyBindings()
    @bindings.add('enter')
    def _(event):
        # Accept the current completion and insert a space
        event.app.current_buffer.insert_text('')
        event.app.current_buffer.complete_state = None

    while True:
        try:
            text = session.prompt(key_bindings=bindings)
            print(f"You entered: {text}")
        except KeyboardInterrupt:
            break  # Control-C pressed
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
