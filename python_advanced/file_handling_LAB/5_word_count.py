import re

WORDS_FILE = 'words.txt'
INPUT_FILE = 'input.txt'


def read_file(name):
    with open(name, 'r') as file:
        read = file.read().lower()
        ll = re.findall(r'[a-z\']+', read)
        return ll


words = read_file(WORDS_FILE)
text = read_file(INPUT_FILE)

collection = {word: text.count(word) for word in words}
sorted_collection = sorted(collection.items(), key=lambda x: -x[1])
print(*[f'{tup[0]} - {tup[1]}' for tup in sorted_collection], sep='\n')
