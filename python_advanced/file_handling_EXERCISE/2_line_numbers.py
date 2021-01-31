READ_PATH = 'text.txt'
WRITE_PATH = 'output,txt'
PUNCTUATION = ("-", ",", ".", "!", "?", "'")


def count_chars(line):
    return len([ch for ch in line if ch.isalnum()])


def count_punctuation(line):
    return len([ch for ch in line if ch in PUNCTUATION])


with open(READ_PATH) as r_file:
    lines = r_file.readlines()

text = ''
count = 1
for line in lines:
    char_count = count_chars(line)
    p_count = count_punctuation(line)
    text += f'Line {count}: {line.strip()} ({char_count})({p_count})\n'
    count += 1

with open(WRITE_PATH, 'w') as w_file:
    w_file.write(text)
