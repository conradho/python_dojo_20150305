
something = [1,2,3,4]

print(something)

def hello(param1):
    """
    A docstring
    """
    print(str(param1))
    return something;

hello(1)

if something == True:
    print(False)

assert(something is not None)

# Do a silly loop
for i in something:
    print(int(i))
