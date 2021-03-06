from rich.text import TextType
from textual.events import Event


class TextChanged(Event):
    """Emmited when the text is changed in the widget"""

    pass


class PyperclipError(Event):
    """Emmited when the text could not be pasted from system clipboard"""

    pass


class InvalidInputAttempt(Event):
    """
    Emitted when a letter in blackist or a letter not in whitelist was being tried to push in the widget
    """

    pass


class ListItemSelected(Event):
    """
    Emitted when a item is selected in the list
    """

    def __init__(self, sender, option: TextType) -> None:
        super().__init__(sender)
        self.selected = option
