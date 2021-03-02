class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(pages=int(1 / 4 * photos_count))

    @staticmethod
    def find_next_free_slot(alb):
        for page in range(len(alb)):
            if len(alb[page]) == 4:
                continue
            return page, len(alb[page])

    def add_photo(self, label: str):
        found_slot = self.find_next_free_slot(self.photos)
        if not found_slot:
            return "No more free spots"
        page, slot = found_slot
        self.photos[page].append(label)
        return f"{label} photo added successfully on page {page + 1} slot {slot + 1}"

    def display(self):
        rep = '-----------\n'
        for page in self.photos:
            rep += ' '.join(['[]' for el in range(len(page))])
            rep += '\n-----------\n'
        return rep

# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
#
# """
# baby photo added successfully on page 1 slot 1
# first grade photo added successfully on page 1 slot 2
# eight grade photo added successfully on page 1 slot 3
# party with friends photo added successfully on page 1 slot 4
# [['baby', 'first grade', 'eight grade', 'party with friends'], []]
# prom photo added successfully on page 2 slot 1
# wedding photo added successfully on page 2 slot 2
# -----------
# [] [] [] []
# -----------
# [] []
# -----------
#
# """
