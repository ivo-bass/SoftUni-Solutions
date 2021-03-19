class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content


class Printer:
    @staticmethod
    def get_book(book: Book, formatter: Formatter):
        return formatter.format(book)