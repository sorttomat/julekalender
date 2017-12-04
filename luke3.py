from PIL import Image

   
def getRed(im, x, y):
    red, g, b = im.getpixel((x, y))
    return red

def getAllReds(im, width, height):
    reds = []
    for y in range(height):
        for x in range(width):
            reds.append(getRed(im, x, y))
    return reds

def sjekkPartall(tall):
    return tall%2 == 0


def decodeByte(byte):
    number = 0
    for i in range(8):
        if byte[i]:
            number += 2**i
    return number

def listToByteArray(lst):
    byter = bytearray(b'\x00\x0f')
    for i in range(0, len(lst), 8):
        byte = decodeByte(lst[i:i+8])
        byter.append(byte)
    return byter
    

def makeLSBList(lst):
    LSBList = []
    for elem in lst:
        if sjekkPartall(elem):
            LSBList.append(False)
        else:
            LSBList.append(True)
    return LSBList   

rgbImage = Image.open("bilde.png")


width, height = rgbImage.size

reds = getAllReds(rgbImage, width, height)

bitList = makeLSBList(reds)

byteArray = listToByteArray(bitList)


resultat = byteArray[0:126].decode('utf-8')
print(resultat)
