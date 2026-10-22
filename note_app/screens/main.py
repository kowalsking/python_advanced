from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header


class MainScreen(Screen):
    BINDIGS = [
        ("q", "quit", "Exit")
    ]
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
    
    def on_mount(self):
        self.title = "Notes Manager"
        
    def action_quit(self):
        self.app.exit()