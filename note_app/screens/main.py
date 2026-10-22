from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Tree, Markdown
from textual.containers import Horizontal


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%
    }
    """
    
    BINDIGS = [
        ("q", "quit", "Exit")
    ]
    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Tree(label="My Knowledge base!", id="tree")
            yield Markdown("# Hello im Header!")
        yield Footer()
    
    def on_mount(self):
        self.title = "Notes Manager"
        
    def action_quit(self):
        self.app.exit()