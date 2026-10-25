
from textual.screen import ModalScreen
from textual.containers import Container, Horizontal
from textual.widgets import Static, Input, Button


class ImportModal(ModalScreen[str]):
    CSS = """
        Screen {
            align: center middle;
        }
        
        #dailog {
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
            yield Input(placeholder="Input URL for import", id="input-url")
            with Horizontal(id="buttons"):
                yield Button('Import', variant="primary", id="import-btn")
                yield Button('Close', id="cancel-btn")
                
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "import-btn":
            url_input = self.query_one("#input-url", Input)
            url = url_input.value.strip()
            if url:
                pass
            else:
                url_input.styles.border = ("solid", "red")
        else:
            self.dismiss(None)
    
    async def import_data(self, url: str) -> None:
        pass