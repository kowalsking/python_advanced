
from textual.screen import ModalScreen
from textual.containers import Container, Horizontal
from textual.widgets import Static, Input, Button


class ImportModal(ModalScreen):
    CSS = """
        Screen {
            align: center middle;
        }
        
        #dailog {
            width: 60;
            height: 15;
            border: solid pink;
        }
        #title {
            dock: top;
            content-align: left middle;
            padding: 0 1;
            height: 2;
        }
        #buttons {
            align: center middle;
        }
    """
    
    
    def compose(self):
        with Container(id="dialog"):
            yield Static("Import data", id="title")
            yield Input(placeholder="Input URL for import")
            with Horizontal(id="buttons"):
                yield Button('Import', variant="primary")
                yield Button('Close')
            