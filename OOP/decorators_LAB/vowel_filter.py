def vowel_filter(function):

    def wrapper():
        vowels = 'a', 'e', 'o', 'u', 'i', 'y'
        return [ch for ch in function() if ch in vowels]

    return wrapper


# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
# print(get_letters())