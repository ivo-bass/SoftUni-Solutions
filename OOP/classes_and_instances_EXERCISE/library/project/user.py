class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []  # in the problem description is described as class attr not instance attr

    @staticmethod
    def check_if_book_is_rented(self, book_name, library):
        for name, dd in library.rented_books.items():
            for book, days in dd.items():
                if book == book_name:
                    return f'The book "{book}" is already rented and will be available in {days} days!'

    def check_if_user_in_rented_books(self, library):
        if not library.rented_books.get(self.username):
            library.rented_books.update({self.username: {}})

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if book_name in library.books_available.get(author):
            self.books.append(book_name)
            self.check_if_user_in_rented_books(library)
            library.rented_books[self.username].update({book_name: days_to_return})
            library.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        return self.check_if_book_is_rented(book_name, library)

    def return_book(self, author: str, book_name: str, library):
        try:
            self.books.remove(book_name)
            library.books_available[author].append(book_name)
            del library.rented_books[self.username][book_name]
        except ValueError:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
