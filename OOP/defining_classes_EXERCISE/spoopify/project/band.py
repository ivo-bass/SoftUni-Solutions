class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for alb in self.albums:
            if alb.name == album_name and not alb.published:
                self.albums.remove(alb)
                return f"Album {album_name} has been removed."
            if alb.name == album_name and alb.published:
                return "Album has been published. It cannot be removed."
        return f"Album {album_name} is not found."

    def details(self):
        info = f"Band {self.name}\n"
        for alb in self.albums:
            info += f"{alb.details()}\n"
        return info
