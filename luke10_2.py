
ansatte = [x for x in range(1, 10)]
tall = 0

while True:
    delete = tall + 2
    if len(ansatte) == 1:
        break
    if delete > len(ansatte):
        tall -= len(ansatte)
    else:
        del ansatte[delete]
        tall += 2
    print(ansatte)
    
    