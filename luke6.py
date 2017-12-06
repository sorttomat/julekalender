newFile = open("HovedstadLatLong.txt", "w")


with open("verda.txt") as infile:
    heading = infile.readline()
    lines = infile.readlines()
    for line in lines:
        if "\tHovedstad" in line:
            line = line.lower()
            line = line.split()
            g = 0
            la = 10
            lo = la + 1
            geoname = line[g]
            while geoname[0].isdigit() == False:
                g += 1
                geoname = line[g]

            latitude = line[la]
            longitude = line[lo]
            while "." not in latitude or latitude[0].isalpha():        
                la += 1
                latitude = line[la]
                longitude = line[la + 1]

            skriv = geoname + " " + latitude + " " + longitude + "\n"
            newFile.write(skriv)        

newFile.close()
infile.close()




