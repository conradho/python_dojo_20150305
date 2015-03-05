#/usr/bin/env python3.4

import sys


def cut_blank_lines(script_path):
    new_file_by_line = []
    with open(script_path, 'r') as python_file:
        for line in python_file.readlines():
            if line.strip() == '':
                continue
            new_file_by_line.append(line)
    print('*'*40, new_file_by_line, '*'*40)
    with open(script_path, 'w') as new_python_file:
        for line in new_file_by_line:
            new_python_file.write(line)

if __name__ == '__main__':
    # takes a script and edits/overwrites it with minimified script
    python_script_path = sys.argv[1]
    cut_blank_lines(python_script_path)
