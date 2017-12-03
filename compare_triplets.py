
def solve(*args):
    # Complete this function
    point_alice = 0
    point_bob = 0
    for ix, k in enumerate(args[:3]):
        if k == args[ix + 3]:
            continue
        if k > args[ix + 3]:
            point_alice += 1
        else:
            point_bob += 1
    print(point_alice, point_bob)
    
a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))