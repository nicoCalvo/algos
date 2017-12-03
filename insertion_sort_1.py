import sys

_len = int(input().strip())
ar = input().strip()

ar = ar.split(' ')
if not ar or _len < 2:
    print(' '.join(ar))
else:
    e = ar[-1]
    ix = len(ar) -2
    while ix >= 0:
        if ar[ix] > e:
            ar[ix+1] = ar[ix]
            print(' '.join(ar))
        elif ar[ix] <= e:
            ar[ix+1] = e
            print(' '.join(ar))
            ix = -3
    
        ix -= 1
    if ix == -1:
        ar[0] = e
        print(' '.join(ar))