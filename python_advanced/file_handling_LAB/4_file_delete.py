import os

PATH = 'my_first_file.txt'

if os.path.exists(PATH):
    os.remove(PATH)
else:
    print('File already deleted!')
