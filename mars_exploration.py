
S = input().strip()
message = 'SOS'
missing_chars = 0
for pos_msg in range(0, len(S), 3):
    sos = S[pos_msg:pos_msg + 3]
    missed = sum([1 if sos[x] != message[x] else 0 for x in range(3)])
    missing_chars += missed
    
print(missing_chars)
