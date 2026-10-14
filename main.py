# class Printer:
#     def print_doc(self, doc: str):
#         pass
    
#     def scan_doc(self, doc: str):
#         pass

#     def fax_doc(self, doc: str):
#         pass
    
# class OldPrinter(Printer):
#     def print_doc(self, doc: str):
#         print(doc)
    
#     def scan_doc(self, doc: str):
#         raise NotImplementedError("Can't!")
    
#     def fax_doc(self, doc: str):
#         raise NotImplementedError("Can't!")

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_doc(self, doc: str): ...

class Scanable(ABC):
    @abstractmethod
    def scan_doc(self, doc: str): ...
    
class Faxable(ABC):
    @abstractmethod
    def fax_doc(self, doc: str): ...
    
class ModernPrinter(Printable, Scanable, Faxable):
    def print_doc(self, doc: str): ...
    def scan_doc(self, doc: str): ...
    def fax_doc(self, doc: str): ...
    
class OldPrinter(Printable):
    def print_doc(self, doc: str): ...