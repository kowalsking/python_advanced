from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Tree
from textual.containers import Horizontal

from note_app.config.config import AppSettings
from note_app.repositories import BaseFolderRepository, BaseNoteRepository
from note_app.screens.import_modal import ImportModal
from note_app.widgets import NoteViewWidget
from note_app.widgets.file_tree import FileTreeWidget


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%
    }
    """
    
    BINDIGS = [
        ("q", "quit", "Exit"),
        ("i", "import", "Import"),
    ]

    def __init__(self,settings: AppSettings,folder_repo: BaseFolderRepository, note_repo: BaseNoteRepository, *args, **kwargs):
        self.settings = settings
        self._folder_repo = folder_repo
        self._note_repo = note_repo
        super().__init__(*args, **kwargs)
    
    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield FileTreeWidget(self._folder_repo, self._note_repo)
            yield NoteViewWidget()
        yield Footer()
    
    def on_mount(self):
        self.title = "Notes Manager"
        
    def action_quit(self):
        self.app.exit()

    def action_import(self):
        self.app.push_screen(ImportModal(), self.handle_import)
        
    def handle_import(self, data):
        pass
        
    def on_file_tree_widget_note_selected(self, message: FileTreeWidget.NoteSelected) -> None:
        note = self._note_repo.load_note(message.note_path)
        if note.content:
            self.query_one(NoteViewWidget).text = note.content
        else:
            self.query_one(NoteViewWidget).text = ''
            