
from textual.screen import ModalScreen
from textual.containers import Container, Horizontal
from textual.widgets import Static, Input, Button
import httpx

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
            yield Input(placeholder="Input URL for import", id="imput-url")
            with Horizontal(id="buttons"):
                yield Button('Import', variant="primary", id="import-btn")
                yield Button('Close', id="cancel-btn")
                
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "import-btn":
            url_input = self.query_one("#imput-url", Input)
            url = url_input.value.strip()
            if url:
                self.app.call_later(self.import_data, url)
            else:
                url_input.styles.border = ("solid", "red")
        else:
            self.dismiss(None)
    
    async def import_data(self, url: str) -> None:
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(url)
                response.raise_for_status()
                data = response.text
                self.dismiss(data)
        except httpx.HTTPError as e:
            self.app.notify(f"Error loader: {e}", severity="error")
        except Exception as e:
            self.app.notify(f"Error unknown")