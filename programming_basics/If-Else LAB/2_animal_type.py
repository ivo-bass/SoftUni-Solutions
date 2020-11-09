animal = input()
animal_class = 'unknown'

if animal == 'dog':
    animal_class = 'mammal'
elif animal in ('crocodile', 'tortoise', 'snake'):
    animal_class = 'reptile'

print(animal_class)
