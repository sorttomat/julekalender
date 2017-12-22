
def tellForekomster(filnavn):
    antallForekomster = {}
    with open(filnavn, "r") as infile:
        for line in infile:
            line = line.strip("\n")
            for elem in line:
                if elem in antallForekomster:
                    antallForekomster[elem] += 1
                else:
                    antallForekomster[elem] = 1
        infile.close()
    return antallForekomster

def dictSortertVerdier(dict):
    sortertKryptert = []
    for num in sorted(dict.values()):
        sortertKryptert.append(list(dict.keys())[list(dict.values()).index(num)])
    return sortertKryptert[::-1]

def lagNøkkel(sortertKryptert, alfabet):
    nøkkel = ""
    for elem in sortertKryptert:
        index = alfabet.index(elem)
        binary = bin(index)
        strBinary = str(binary)[2::]
        if len(strBinary) < 5:
            antall = 5 - len(strBinary)
            nuller = "0" * antall
            strBinary = nuller + strBinary
        nøkkel += strBinary
    return nøkkel

def bitsTilBytes(bits):
    byter = bytearray(b'\x00\x0f')
    for i in range(0,len(bits), 8):
        byte = int(bits[i:i+8], 2)
        byter.append(byte)
    return byter

def dekoder(byter):
    return byter.decode('utf-8')

def xor(kryptert, nøkkel):
    nøkkelXORKryptert = int(nøkkel, 2)^int(kryptert,2)
    return str((bin(nøkkelXORKryptert)[2:].zfill(len(nøkkel))))
    


alfabet = "AÁBDÐEÉFGHIÍJKLMNOÓPRSTUÚVXYÝÞÆÖ"
kryptert = "1110010101000001011000000011101110100101010011011010101101100000010001111101000001010010001011101001100100100011010000110101111101010011100010110001100111110010"

antallForekomster = tellForekomster("text.txt")

sortertKryptert = dictSortertVerdier(antallForekomster)

nøkkel = lagNøkkel(sortertKryptert, alfabet)

print(dekoder(bitsTilBytes(xor(kryptert, nøkkel))))
