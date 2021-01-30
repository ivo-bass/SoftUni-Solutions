import os

F_PATH = 'text.txt'

if os.path.exists(F_PATH):
    with open(F_PATH):
        print('File found')
else:
    print('File not found')
