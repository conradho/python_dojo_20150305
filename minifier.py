import ast
import re

infile = 'test.py'
builtin_stuff = ['print', True, False, None, 'str', 'bool']

file = open(infile).read()
parsed = ast.parse(file)

def get_variable_names(tree):
    names = []
    for node in tree:
        if isinstance(node, ast.Assign):
            names.append(node.targets[0].id)

    return names

def parse_functions(tree):
    function_names = []
    function_params = []
    for node in tree:
        if isinstance(node, ast.FunctionDef):
            function_names.append(node.name)
            for arg in node.args.args:
                function_params.append(arg.arg)
    return function_names, function_params

variables = get_variable_names(parsed.body)
functions, params = parse_functions(parsed.body)

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
for p in params:
    modified_file = re.sub(p, next(char_generator), modified_file)

for builtin in builtin_stuff:
    char = next(char_generator)
    line = "%s=%s;" % (char, str(builtin))
    modified_file = re.sub(str(builtin), char, modified_file)
    modified_file = line + modified_file
print(modified_file)
