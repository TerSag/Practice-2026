from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title
    @abstractmethod
    def get_description(self): pass


class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.__author = author 
    
    def get_description(self):
        return f"Книга: '{self.title}', автор: {self.__author}"

class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow(self, item: LibraryItem):
        self.books.append(item)
        print(f"{self.name} взяв: {item.get_description()}")

lib_item = Book("Кобзар", "Т. Шевченко")
user = Reader("Дмитро")
user.borrow(lib_item)