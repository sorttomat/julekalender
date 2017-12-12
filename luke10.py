ansatte = [x for x in range(1, 1501)]
start = 1
while len(ansatte) != 1:
    lenForrige = len(ansatte)

    del ansatte[start::2]

    if lenForrige % 2 != 0:
        start ^= 1  

print(ansatte)

