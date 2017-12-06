

dic = {}
with open("HovedstadLatLong.txt", "r") as infile:
    lines = infile.readlines()
    for line in lines:
        words = line.split()
        dic[words[0]] = [float(words[1]), float(words[2])]

infile.close()





for key in dic:
    latDest = dic[key][0]
    longDist = dic[key][1]
    avstand = getDistanceFromLatLng(latitudeOslo, longOslo, latDest, longDist)
    dic[key].append(avstand)

#Program:


avstander = []
for key in dic:
    avstander.append(dic[key][2])

avstander = sorted(avstander)
