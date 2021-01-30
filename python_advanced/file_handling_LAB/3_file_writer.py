F_NAME = 'my_first_file.txt'
TEXT = 'I just created my first file!'

with open(F_NAME, 'w') as file:
    file.write(TEXT)
