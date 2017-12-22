gaver = 0

for i in range(1025):
    sm = 0
    for j in range(i+1):
        sm += j
    gaver += sm

print(gaver) 