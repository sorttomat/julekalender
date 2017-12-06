from math import radians, cos, sin, asin, sqrt
# Distance between two lat/lng coordinates in km using the Haversine formula
def getDistanceFromLatLng(latOslo, lngOslo, latDest, lngDest): # use decimal degrees
    r=6371 # radius of the earth in km
    latOslo=radians(latOslo)
    latDest=radians(latDest)
    lat_dif=latDest-latOslo
    lng_dif=radians(lngDest-lngOslo)
    a=sin(lat_dif/2.0)**2+cos(latOslo)*cos(latDest)*sin(lng_dif/2.0)**2
    d=2*r*asin(sqrt(a))
    return d # return km

dic = {}
with open("HovedstadLatLong.txt", "r") as infile:
    lines = infile.readlines()
    for line in lines:
        words = line.split()
        dic[words[0]] = [float(words[1]), float(words[2])]

infile.close()

latitudeOslo = 59.911491
longOslo = 10.757933



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

fart = 7274 #km/h
totalDrivstoff = fart * 24 #timer
nesteDest = avstander[0]* 2
antallReiser = 0
teller = 0

while totalDrivstoff - nesteDest > 0:
    antallReiser += 1
    totalDrivstoff -= nesteDest
    teller += 1
    nesteDest = avstander[teller] * 2


print(antallReiser)