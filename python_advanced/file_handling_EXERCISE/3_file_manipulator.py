import os

END_COMMAND = 'End'
CREATE = 'Create'
ADD = 'Add'
REPLACE = 'Replace'
DELETE = 'Delete'
ERROR_MSG = 'An error occurred'


def create_file(name):
    with open(name, 'w') as file:
        file.write('')


def add_content(name, content):
    with open(name, 'a') as file:
        file.write(content + '\n')


def replace_text(name, old, new):
    if not os.path.exists(name):
        print(ERROR_MSG)
        return
    with open(name, 'r') as r_file:
        reader = r_file.read()
        updated = reader.replace(old, new)
    with open(name, 'w') as w_file:
        w_file.write(updated)


def delete_file(name):
    if os.path.exists(name):
        os.remove(name)


while True:
    command = input()
    if command == END_COMMAND:
        break
    action, *data = command.split('-')
    if action == CREATE:
        name = data[0]
        create_file(name)
    elif action == ADD:
        name, content = data
        add_content(name, content)
    elif action == REPLACE:
        name, old, new = data
        replace_text(name, old, new)
    elif action == DELETE:
        name = data[0]
        delete_file(name)
