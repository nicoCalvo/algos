s_len = int(input().strip())
s = input().strip()
s = [int(x) for x in s.split(' ')]
ix = 0
s_len -= 1
while ix < s_len:
    pos = ix
    if pos < s_len and s[pos] > s[pos + 1]:
        _var = s[pos]
        s[pos] = s[pos + 1]
        s[pos + 1] = _var
        pos += 1
    pos = ix
    while pos > 0 and s[pos] < s[pos - 1]:
        _var = s[pos]
        s[pos] = s[pos - 1]
        s[pos - 1] = _var
        pos -= 1
    print(' ' .join([str(x) for x in s]))
    ix += 1
