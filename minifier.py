import ast
import re

infile = 'test.py'

file = open(infile).read()
parsed = ast.parse(file)

def get_variable_names(tree):
    names = []
    for node in tree:
        if isinstance(node, ast.Assign):
            names.append(node.targets[0].id)

    return names

def get_function_names(tree):
    names = []
    for node in tree:
        if isinstance(node, ast.FunctionDef):
            names.append(node.name)
    return names

variables = get_variable_names(parsed.body)
functions = get_function_names(parsed.body)

def get_next_char(i):
    while True:
        yield chr(i)
        i += 1

#import ipdb; ipdb.set_trace()
# Will start at kanji/hanzi
char_generator = get_next_char(30000)

modified_file = ""
for f in functions:
     modified_file = re.sub(f, next(char_generator), file)
for v in variables:
    modified_file = re.sub(v, next(char_generator), modified_file)

print(modified_file)
