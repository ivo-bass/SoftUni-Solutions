phonebook = {}
the_input = None
while True:
    the_input = input()
    if the_input.isnumeric():
        break
    name, number = the_input.split('-')
    phonebook[name] = number

n = int(the_input)
for _ in range(n):
    contact = input()
    if contact in phonebook:
        print(f'{contact} -> {phonebook[contact]}')
    else:
        print(f'Contact {contact} does not exist.')
