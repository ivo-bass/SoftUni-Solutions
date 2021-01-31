from custom_functions import create_file, add_content, replace_text, delete_file

END_COMMAND = 'End'

mapper = {
    'Create': create_file,
    'Add': add_content,
    'Replace': replace_text,
    'Delete': delete_file,
}

while True:
    command = input()
    if command == END_COMMAND:
        break
    action, *args = command.split('-')
    mapper[action](*args)
