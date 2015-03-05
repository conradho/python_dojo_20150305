#/usr/bin/env python3.4

import sys


def cut_blank_lines(script_path):
    lines = []
    with open(script_path, 'r') as python_file:
        for line in python_file.readlines():
            if line.strip() == '':
                continue
            lines.append(line)
    return ''.join(lines)

if __name__ == '__main__':
    # takes a script and edits/overwrites it with minimified script
    python_script_path = sys.argv[1]
    cut_blank_lines(python_script_path)
