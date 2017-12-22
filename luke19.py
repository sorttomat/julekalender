from turtle import *

with open("path.txt", "r") as infile:
    for line in infile:
        line = line.strip()
        line = line.split(",")
        direction = line[1].strip(" ")
        amount = int(line[0])
        if direction == "east":
            heading = 0
        elif direction == "west":
            heading = 180
        elif direction == "north":
            heading = 90
        else: #south
            heading = 270
        setheading(heading)
        forward(amount)
    setheading(180)
    forward(200)
    infile.close()
    done()