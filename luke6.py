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

def hentAvstander(filename, latitudeOslo, longitudeOslo):
    avstander = []
    with open(filename) as infile:
        heading = infile.readline()
        lines = infile.readlines()
        geokoder = []
        for line in lines:
            if "\tHovedstad" in line:
                line = line.lower()
                line = line.split("\t")
                if line[4] not in geokoder:
                    latitude = float(line[12])
                    longitude = float(line[13])
                    avstander.append(getDistanceFromLatLng(latitudeOslo, longitudeOslo, latitude, longitude))
                    geokoder.append(line[4])
    infile.close()
    return sorted(avstander)


latitudeOslo = 59.911491
longitudeOslo = 10.757933
fart = 7274 #km/h
totalDrivstoff = fart * 24 #timer

avstander = hentAvstander("verda.txt", latitudeOslo, longitudeOslo)


nesteDest = avstander[0]* 2
antallReiser = 0
teller = 0

while totalDrivstoff - nesteDest > 0:
    antallReiser += 1
    totalDrivstoff -= nesteDest
    teller += 1
    nesteDest = avstander[teller] * 2

print(antallReiser)





