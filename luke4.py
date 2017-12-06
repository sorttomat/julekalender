
def erPartall(tall):
    return tall % 2 == 0

def checkElementInThing(thing, element):
    antall = 0
    for elem in thing:
        if elem == element:
            antall += 1
    return antall

def numberOfEachLetter(word):
    antBokstaver = []
    for bokstav in word:
        antBokstaver.append(checkElementInThing(word, bokstav))
        word = word.replace(bokstav, "")

    return antBokstaver

def sjekkMulighet(lst):
    partallOddetall = []
    for elem in lst:
        if erPartall(elem):
            partallOddetall.append(True)
        else:
            partallOddetall.append(False)
            print(False)        
    if checkElementInThing(partallOddetall, False) == 1 or checkElementInThing(partallOddetall, False) == 0:
        return True
    return False

def checkPalendrome(word):
    antBokstaver = numberOfEachLetter(word)
    if sjekkMulighet(antBokstaver) or len(word) == 0 or len(word) == 1:
        return True
    return False

def checkAlreadyPalendrome(word):
    if word == word[::-1]:
        return True
    return False

def checkAllWords(filename, newFilename):
    palindromes = open(newFilename, "w")
    count = 0
    with open(filename, "r") as infile:
        for line in infile:
            word = line.strip("\n")
            word = word.strip("-")
            word = word.lower()
            if checkPalendrome(word) and checkAlreadyPalendrome(word) == False:
                palindrome = word + "\n"
                palindromes.write(palindrome)
                count += 1

    palindromes.write("Number of palindromes: \n")
    palindromes.write(str(count))
    palindromes.close()
    infile.close()

                                

checkAllWords("anagramlist.txt", "listoveranagrams.txt")


