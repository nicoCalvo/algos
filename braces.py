
def braces(values):
    resp = []
    pairs = {}
    pairs['('] = ')'
    pairs['{'] = '}'
    pairs['['] = ']'
    for string in values:
        stack_open = []
        balanced = True
        ix = 0
        while balanced and ix < len(string):
            if string[ix] in pairs:
                stack_open.append(string[ix])
            else:
                if not stack_open or string[ix] != pairs[stack_open[-1]]:
                    balanced = False
                else:
                    stack_open.pop()
            ix += 1
        resp.append('YES' if balanced else 'NO')
    return resp

res = braces(['{}[]()', '{[}]}', ''])
print(res)