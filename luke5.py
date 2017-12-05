import time
start_time = time.time()
listNumbers = [0, 1, 2, 2, 3, 3]
# tallTxt= open("tall.txt", "w")

# for tall in listNumbers:
#    skriv = str(tall) + "\n"
#    tallTxt.write(skriv)

tall = 4 #Starter her
while len(listNumbers) < 1000000:
    antall = listNumbers[tall]
    for j in range(antall):
        listNumbers.append(tall)
        # skriv = str(tall) + "\n"
        # tallTxt.write(skriv)
    tall += 1

# tallTxt.close()

sumTall = sum(listNumbers[0:1000001])

print(sumTall)



print("--- %s seconds ---" % (time.time() - start_time))