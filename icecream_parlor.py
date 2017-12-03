
def icecream_parlor(bucks, n_flavors, flavors):
    n_icecream = 0
    flavors_candidates = []
    while n_icecream < n_flavors:
        if flavors[n_icecream] < bucks:
            flavors_candidates.append(n_icecream)
        n_icecream += 1
    pos = 0
    match = False
    while not match and pos < len(flavors_candidates):
        pos2 = pos +1
        flavor1_cost = flavors[flavors_candidates[pos]]
        
        while not match and pos2 < len(flavors_candidates):
            if flavors[flavors_candidates[pos2]] + flavor1_cost == bucks:
                print(flavors_candidates[pos] +1 , flavors_candidates[pos2] + 1)
                match = True
            pos2 += 1
        pos += 1

        
trips = int(input().strip())
bucks = []
n_flavors = []
flavors = []
pos = 0
while pos < trips:
    bucks.append(int(input().strip()))
    n_flavors.append(int(input().strip()))
    flavors.append(str(input().strip()))
    pos += 1
for trip in range(trips):
    flavors2 = [int(x) for x in flavors[trip].split(' ')]
    icecream_parlor(bucks[trip], n_flavors[trip], flavors2)