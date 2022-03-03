def unwrapCSS(file, result="result.txt", indentsize=4):
    with open(file, 'r') as infile:
        data = infile.readlines()[0]
    res = ''
    for char in data:
        if char not in [';', '{', '}']:
            res += char
            continue
        if char == '{' or char == ';':
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