READ_PATH = 'text.txt'
WRITE_PATH = 'output,txt'
PUNCTUATION = ("-", ",", ".", "!", "?", "'")


with open(READ_PATH) as r_file:
    lines = r_file.readlines()


new_lines = []
for i in range(len(lines)):
    char_count = 0
    for char in lines[i]:
        if char.isalnum():
            char_count += 1
    p_count = 0
    for p in PUNCTUATION:
        p_count += lines[i].count(p)
    line = f'Line {i+1}: ' + lines[i].rstrip() + f' ({char_count})({p_count})'
    new_lines.append(line)


with open(WRITE_PATH, 'w') as w_file:
    w_file.write('\n'.join(new_lines))
