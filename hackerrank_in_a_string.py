import sys

WORD = 'hackerrank'
len_WORD = len(WORD) -1
q = int(input().strip())

for a0 in range(q):
    s = input().strip()
    pos = 0
    it_is = False
    for char in s:
        if pos == len_WORD :
            it_is = True
            pos = 0
        if char == WORD[pos]:
            pos += 1
         
    if it_is:
        print('YES')
    else:
        print('NO')