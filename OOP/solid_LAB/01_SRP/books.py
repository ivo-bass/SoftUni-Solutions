class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.books.append(book)


class TakenBook:
    def __init__(self, book):
        self.book = book
        self.page = 0

    def go_to_page(self, page):
        self.page = page

    def next_page(self):
        self.page += 1
