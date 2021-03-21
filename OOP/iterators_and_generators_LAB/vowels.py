class vowels:
    VOWELS = ('a', 'e', 'o', 'u', 'i', 'y')

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.string):
            raise StopIteration
        char = self.string[self.index]
        self.index += 1
        if not self.is_vowel(char):
            return self.__next__()
        return char

    def is_vowel(self, char):
        return char.lower() in self.VOWELS

#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)