
from abc import ABC, abstractmethod
from pathlib import Path
import shutil

from note_app.domain import Folder
from note_app.repositories.base_folder_repository import BaseFolderRepository


class FolderRepository(BaseFolderRepository):
    def __init__(self, base_path: Path) -> None:
        self.base_path = base_path.resolve()
    
    def _check_path(self, path: Path):
        if not path.exists() or not path.is_dir():
            raise ValueError(f'Folder doesnt exist: {path}')

        if self.base_path not in path.parents and path != self.base_path:
            raise ValueError("Access outside data directory is not allowed")
        
    def get_folders_by_path(self, path: Path) -> list[Folder]:
        path = path.resolve()
        
        self._check_path(path)
        
        folders: list[Folder] = []
        
        for sub_path in path.iterdir():
            if sub_path.is_dir() and not sub_path.name.startswith('.'):
                folders.append(
                    Folder(
                        name=sub_path.name,
                        path=sub_path
                    )
                )
                
        return sorted(folders, key=lambda f: f.name)
    
    def create_folder(self, path: Path, name: str) -> Folder:
        self._check_path(path)
        
        if not name or "/" in name or "\\" in name:
            raise ValueError("Invalid folder name")
        path.mkdir(parents=True, exist_ok=False)        
        return Folder(name, path)

    
    def delete_folder(self, folder: Folder) -> None:
        path = folder.path.resolve()
        self._check_path(path)
        
        if path == self.base_path:
            raise ValueError('Can"t delete base path')

        shutil.rmtree(path)