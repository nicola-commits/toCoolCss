import re #for regex
def wrap(file):
    return ''.join([item.strip() for item in open(file, 'r').readlines()])

def unwrapCSS(file, result="result.txt", indentsize=4):
    with open(file, 'r') as infile:
        data = infile.readlines()[0]
    res = ''
    for char in data:
        if char not in [';', '{', '}']:
            res += char
        elif char in ['{', ';']:
            res += char
            res += '\n'
            res += ' '*indentsize
        else:
            res += '\n'
            res += char
            res += '\n'
    if res[-1] == '\n':
        res = res[:-1]
    with open(result, 'w') as infile:
        infile.write(res)

def unwrapJS(file, result="result.txt", indentsize=4, text=False):
    """
    First read the data
    next identify tokens that require a newline and those that require more indent
    second separate it between the tokens
    add it all together
    write into result
    """
    #1
    if text:
        data = file
    else:
        with open(file, 'r') as infile:
            data = infile.read()
    #2
    newlines = [';']
    moreindent = ['{']
    lessindent = ['}']
    indent = 0
    res = ''
    last = ''
    for char in data:
        if char in newlines:
            res += char
            res += '\n'
            res += ' '*indent
        elif char in moreindent:
            res += char
            res += '\n'
            indent += indentsize
            res += ' '*indent
        elif char in lessindent:
            if last == ';':
                res = res[:-indentsize]
            indent -= indentsize
            res += ' '*indent
            res += char
        else:
            res += char
        last = char
    with open(result, 'w') as infile:
        infile.write(res)