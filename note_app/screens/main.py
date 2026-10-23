from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Tree
from textual.containers import Horizontal

from note_app.widgets import MarkdownWidget


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
            yield MarkdownWidget()
        yield Footer()
    
    def on_mount(self):
        self.title = "Notes Manager"
        self.query_one(MarkdownWidget).text = '## Hello!'
        
    def action_quit(self):
        self.app.exit()