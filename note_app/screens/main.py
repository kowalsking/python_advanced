from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Tree
from textual.containers import Horizontal

from note_app.config.config import AppSettings
from note_app.widgets import NoteViewWidget
from note_app.widgets.file_tree import FileTreeWidget
from note_app.repositories import FolderRepository


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%
    }
    """
    
    BINDIGS = [
        ("q", "quit", "Exit")
    ]
    
    def __init__(self,settings: AppSettings, *args, **kwargs):
        self.settings = settings
        super().__init__(*args, **kwargs)
    
    def compose(self) -> ComposeResult:
        folder_repo = FolderRepository(self.settings.data_directory)
        yield Header()
        with Horizontal():
            yield FileTreeWidget(folder_repo)
            yield NoteViewWidget()
        yield Footer()
    
    def on_mount(self):
        self.title = "Notes Manager"
        self.query_one(NoteViewWidget).text = '## Hello!'
        
    def action_quit(self):
        self.app.exit()