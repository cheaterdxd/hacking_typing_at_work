from prompt_toolkit import Application
from prompt_toolkit.layout.containers import VSplit, Window, HSplit, FloatContainer, Float
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Button, Dialog

def create_popup():
    """Creates a simple pop-up dialog."""

    def ok_clicked():
        app.exit()

    ok_button = Button(text='OK', handler=ok_clicked)

    dialog = Dialog(
        title='Information',
        body=Window(FormattedTextControl('This is a pop-up message!'), height=1, style='class:dialog.body'),
        buttons=[ok_button],
        modal=True
    )

    return dialog

def main():
    """Main application."""

    popup = create_popup()

    root_container = FloatContainer(
        content=Window(FormattedTextControl('Press any key to show the popup.'), height=1),
        floats=[
            Float(
                content=popup,
                xcursor=True,
                ycursor=True,
                left=None,
                right=None,
                top=None,
                bottom=None
            )
        ]
    )

    layout = Layout(root_container)

    style = Style.from_dict({
        'dialog':             'bg:#888888',
        'dialog.body':        'bg:#AAAAAA',
        'dialog frame.label': 'bg:#ffffff #000000',
        'dialog.button':      'bg:#cccccc',
        'dialog shadow':      'bg:#000000',
    })

    app = Application(layout=layout, style=style, full_screen=True)
    app.run()

if __name__ == '__main__':
    main()