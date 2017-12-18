a = "AÁBDÐEÉFGHIÍJKLMNOÓPRSTUÚVXYÝÞÆÖ"
alfabet = []

for elem in a:
    alfabet.append(elem)

antallForekomster = {}

with open("text.txt", "r") as infile:
    for line in infile:
        line = line.strip("\n")
        for elem in line:
            if elem in antallForekomster:
                antallForekomster[elem] += 1
            else:
                antallForekomster[elem] = 1
    infile.close()

sortertKryptert = []
for num in sorted(antallForekomster.values()):
    sortertKryptert.append(list(antallForekomster.keys())[list(antallForekomster.values()).index(num)])

sortertKryptert = sortertKryptert[::-1]
print(sortertKryptert)