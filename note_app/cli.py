from pathlib import Path
import sys

from note_app.app import NoteManagerApp
from note_app.config.config import AppSettings


def create_app(data_path: Path | None = None):
    settings: AppSettings
    if data_path:
        settings = AppSettings.from_custom_path(data_path)
    else:
        settings = AppSettings.from_defaults()
    return NoteManagerApp(settings)

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

def letter():
    yield from "ABC"

def run():
    # data_path = None
    # if len(sys.argv) > 1:
    #     data_path = Path(sys.argv[1])
    # app = create_app(data_path)
    # app.run()
    gen = count_up_to(3)
    print(gen)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    
    number = (i for i in range(10))
    print(next(number))
    print(next(number))
    print(letter())
    print(letter())
    