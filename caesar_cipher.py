import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())


final_string = []
final_string = []
for x in s:
    pos = ord(x)
    if not x.isalpha():
        final_string.append(x)
        continue
    _max, _min = (90, 65) if x.istitle() else (122, 97)

    if (k + pos) > _max:
        pos = ( (pos -_min+k) %26 ) + _min
    else:
        pos += k
    final_string.append(chr(pos))
print(''.join(final_string))
