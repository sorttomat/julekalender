alleBokstaver = [[1, 2, 3, 4], [4, 5, 6, 7, 8, 9], [4], [9, 3, 4, 5, 6]]


tall = None
for num in alleBokstaver[0]:
    ja = []
    for i in range(1, len(alleBokstaver)):
        if num in alleBokstaver[i]:
            ja.append(True)
    
    if len(ja) == len(alleBokstaver) - 1:
        tall = num

#print(tall)



tall = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(6 in tall)  