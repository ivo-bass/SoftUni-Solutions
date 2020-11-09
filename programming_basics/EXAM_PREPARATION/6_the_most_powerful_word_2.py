from math import floor

words_list = []
results_list = []
vowels = ('a', 'x', 'e', 'o', 'u', 'y', 'A', 'I', 'E', 'U', 'O', 'Y')

while True:
    raw_word = input()
    word = raw_word.replace(" ,'()!-._=+*/\\\"", "")
    if word == "End of words":
        break
    else:
        ascii_sum = 0
        for i in range(len(word)):
            char = word[i]
            char_value = ord(char)
            ascii_sum += char_value
        if word[0] in vowels:
            result = ascii_sum * len(word)
        else:
            result = floor(ascii_sum / len(word))
        words_list.append(word)
        results_list.append(result)

best_word = ""
best_result = 0
if len(words_list) > 0:
    for r in results_list:
        if r > best_result:
            best_result = r
            best_word = words_list[results_list.index(best_result)]

print(f"The most powerful word is {best_word} - {best_result}")
