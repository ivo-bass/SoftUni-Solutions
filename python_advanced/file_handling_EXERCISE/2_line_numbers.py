import string

READ_PATH = 'text.txt'
WRITE_PATH = 'output.txt'


def count_symbols(line, validation):
    return len([ch for ch in line if ch in validation])


with open(READ_PATH, 'r') as r_file:
    with open(WRITE_PATH, 'w') as w_file:
        reader = r_file.readlines()
        for index, line in enumerate(reader):
            char_count = count_symbols(line, string.ascii_letters)
            p_count = count_symbols(line, string.punctuation)
            print(f'Line {index+1}: {line.strip()} ({char_count})({p_count})',
                  file=w_file)
