import os

ERROR_MSG = 'An error occurred'


def create_file(*args):
    name = args[0]
    with open(name, 'w') as file:
        file.write('')


def add_content(*args):
    name, content = args
    with open(name, 'a') as file:
        file.write(content + '\n')


def replace_text(*args):
    name, old, new = args
    try:
        with open(name, 'r+') as file:
            reader = file.read()
            updated = reader.replace(old, new)
            file.seek(0)
            file.write(updated)
    except FileNotFoundError:
        print(ERROR_MSG)


def delete_file(*args):
    name = args[0]
    if os.path.exists(name):
        os.remove(name)
