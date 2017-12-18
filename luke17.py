def endreTall(tall):
    nyttTall = int("6" + str(tall)[:-1])
    return nyttTall

n = 6
while True:
    tall = n
    nyttTall = endreTall(tall)
    if nyttTall / 4 == tall:
        print("Done! ", tall, nyttTall)
        break
    n += 10