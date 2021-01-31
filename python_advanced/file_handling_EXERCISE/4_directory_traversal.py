import os

TEST_PATH = '/home/iai/SoftUni-Solutions/python_advanced/file_handling_EXERCISE'
ROOT_PATH = './'
USERNAME = os.getlogin()
WIN_REPORT_PATH = f'C:\\Users\\{USERNAME}\\Desktop\\report.txt'
LINUX_REPORT_PATH = f'/home/{USERNAME}/Desktop/report.txt'


def traverse_path(path):
    all_files = {}
    path = os.walk(path)

    for _, _, files in path:
        for file in files:
            index = file.index('.')
            extension = file[index:]
            if not extension in all_files:
                all_files[extension] = []
            all_files[extension].append(file)
    return all_files


def sort_dirs(dd):
    return dict(sorted(dd.items(), key=lambda x: x[0]))


def sort_files(ll):
    return sorted(ll, key=lambda x: x)


def write_report(dd, path):
    with open(path, 'w') as f:
        for ext, names in dd.items():
            f.writelines(ext + '\n')
            sorted_files = sort_files(names)
            for file in sorted_files:
                f.writelines(f'- - - {file}\n')


# Use ROOT_PATH for your system
files = traverse_path(TEST_PATH)
ordered_dirs = sort_dirs(files)
# Use WIN_REPORT_PATH for Windows
write_report(ordered_dirs, LINUX_REPORT_PATH)
