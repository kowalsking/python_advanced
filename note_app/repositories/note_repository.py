
from abc import ABC, abstractmethod
from pathlib import Path
import shutil
from typing import Optional

from note_app.domain import Folder
from note_app.domain import Note
from note_app.repositories.base_note_repository import BaseNoteRepository


class NoteRepository(BaseNoteRepository):
    def __init__(self, base_path: Path) -> None:
        self.base_path = base_path.resolve()
    
    def _check_path(self, path: Path):
        if not path.exists() or not path.is_dir():
            raise ValueError(f'Folder doesnt exist: {path}')

        if self.base_path not in path.parents and path != self.base_path:
            raise ValueError("Access outside data directory is not allowed")
        
    def get_notes_by_path(self, path: Path) -> list[Note]:
        path = path.resolve()
        
        self._check_path(path)
        
        notes: list[Note] = []
        
        for sub_path in path.iterdir():
            if sub_path.is_file() and not sub_path.name.startswith('.') and sub_path.suffix == ".md":
                notes.append(
                    Note(
                        name=sub_path.name,
                        path=sub_path
                    )
                )
                
        return sorted(notes, key=lambda f: f.name)
    
    def create_note(self, path: Path, name: str, content: str) -> Note:
        self._check_path(path)
        
        if not name or "/" in name or "\\" in name:
            raise ValueError("Invalid note name")
        
        new_path = path / f"{name}.md"     
        new_path.write_text(content, encoding='utf-8')
        return Note(name, path)
    
    def update_note(self, note: Note, content: str, new_name: Optional[str] = None) -> Note:
        path = note.path.resolve()
        self._check_path(path)

        path.write_text(content, encoding="utf-8")

        if new_name and new_name != note.name:
            if "/" in new_name or "\\" in new_name:
                raise ValueError("Invalid Note Name")
            new_path = path.parent / f"{new_name}.md"
            path.rename(new_path)
            return Note(new_name, new_path)
        return note

    
    def delete_note(self, note: Note) -> None:
        path = note.path.resolve()
        path.unlink()
        
    def load_note(self, path: Path) -> Note:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            return Note(
                path.name,
                path,
                content
            )