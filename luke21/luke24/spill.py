minst = 20000

portaler = []

infile = open("portals.txt")
lines = infile.readlines()
for line in lines:
    line = line.strip("\n")
    fra, til = line.split("->")
    portaler.append([fra, til])

print(lines[0])
print(portaler[0])
    


