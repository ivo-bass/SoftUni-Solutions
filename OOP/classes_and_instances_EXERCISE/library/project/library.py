class Library:
    def __init__(self):
        self.user_records = []  # [user objects]
        self.books_available = {}  # {author: [books for the author]}
        self.rented_books = {}  # {username: {book: days to return}}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        try:
            self.user_records.remove(user)
            if self.rented_books.get(user.username):
                del self.rented_books[user.username]
        except ValueError:
            return "We could not find such user to remove!"

    def update_rented_books_username(self, u, new_username):
        for name, dd in self.rented_books.items():
            if name == u.username:
                del self.rented_books[name]
                self.rented_books[new_username] = dd
                break

    def change_username(self, user_id: int, new_username: str):
        for u in self.user_records:
            if u.user_id == user_id:
                if u.username == new_username:
                    return "Please check again the provided username - " \
                           "it should be different than the username used so far!"
                self.update_rented_books_username(u, new_username)
                u.username = new_username
                return f"Username successfully changed to: {u.username} for userid: {u.user_id}"
        return f"There is no user with id = {user_id}!"
