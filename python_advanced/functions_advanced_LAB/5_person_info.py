def get_info(**kwargs):
    return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
