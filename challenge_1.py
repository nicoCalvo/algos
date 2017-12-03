
v = str(input().strip())
n = int(input().strip())
ar = str(input().strip())


partial_elm = []
new_ar = []

for elm in ar:
    if not elm.isdigit() and elm != '-':
        new_ar.append(''.join(partial_elm))
        partial_elm = []
    else:
        partial_elm.append(elm)
   
if partial_elm:
    new_ar.append(''.join(partial_elm))
not_found = True
pos = 0
while not_found and pos < n:
    if new_ar[pos] == v:
        not_found = False
    else:
        pos += 1
    
if not not_found:
    print(pos)
