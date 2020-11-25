from re import compile, IGNORECASE

sentence = input()
word = input()

compiled = compile(f"\\b{word}\\b", IGNORECASE)
words = compiled.findall(sentence)

print(len(words))
