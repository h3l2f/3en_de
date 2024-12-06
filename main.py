def encode(s:str, re:bool=False):
    ech = {
        "000000": "A", 
        "000001": "B", 
        "000010": "C",
        "000011": "D",
        "000100": "E", 
        "000101": "F", 
        "000110": "G",
        "000111": "H",
        "001000": "I",
        "001001": "J",
        "001010": "K", 
        "001011": "L", 
        "001100": "M",
        "001101": "N",
        "001110": "O",
        "001111": "P",
        "010000": "Q",
        "010001": "R",
        "010010": "S",
        "010011": "T",
        "010100": "U",
        "010101": "V",
        "010110": "W",
        "010111": "X",
        "011000": "Y",
        "011001": "Z",
        "011010": "a",
        "011011": "b",
        "011100": "c",
        "011101": "d",
        "011110": "e",
        "011111": "f",
        "100000": "g",
        "100001": "h",
        "100010": "i",
        "100011": "j",
        "100100": "k",
        "100101": "l",
        "100110": "m",
        "100111": "n",
        "101000": "o",
        "101001": "p",
        "101010": "q",
        "101011": "r",
        "101100": "s",
        "101101": "t",
        "101110": "u",
        "101111": "v",
        "110000": "w",
        "110001": "x",
        "110010": "y",
        "110011": "z",
        "110100": "0",
        "110101": "1",
        "110110": "2",
        "110111": "3",
        "111000": "4",
        "111001": "5",
        "111010": "6",
        "111011": "7",
        "111100": "8",
        "111101": "9",
        "111110": "+",
        "111111": "/"
    }
    binary = ""
    ls = []
    for i in s:
        if len(format(ord(i), 'b').zfill(8)) > 8:
            raise ValueError("The string to be encoded contains characters outside of the Latin1 range.")
        ls.append(format(ord(i), 'b').zfill(8))
    binary = "".join(ls)
    ls = []
    for i in range(1, len(binary)//6+1):
        ls.append(binary[(i*6)-6: i*6])
    if (len(binary)%6!=0): ls.append(((binary[(len(binary)//6)*6:][::-1]).zfill(6))[::-1])
    en = list("".join(ech[i] for i in ls))
    for i in range((len(en)//2)*2):
        if i%2!=0: continue
        en[i], en[i+1] = en[i+1], en[i]
    return "".join(en)

def decode(s:str, re:bool=False):
    ech = {
        "000000": "A", 
        "000001": "B", 
        "000010": "C",
        "000011": "D",
        "000100": "E", 
        "000101": "F", 
        "000110": "G",
        "000111": "H",
        "001000": "I",
        "001001": "J",
        "001010": "K", 
        "001011": "L", 
        "001100": "M",
        "001101": "N",
        "001110": "O",
        "001111": "P",
        "010000": "Q",
        "010001": "R",
        "010010": "S",
        "010011": "T",
        "010100": "U",
        "010101": "V",
        "010110": "W",
        "010111": "X",
        "011000": "Y",
        "011001": "Z",
        "011010": "a",
        "011011": "b",
        "011100": "c",
        "011101": "d",
        "011110": "e",
        "011111": "f",
        "100000": "g",
        "100001": "h",
        "100010": "i",
        "100011": "j",
        "100100": "k",
        "100101": "l",
        "100110": "m",
        "100111": "n",
        "101000": "o",
        "101001": "p",
        "101010": "q",
        "101011": "r",
        "101100": "s",
        "101101": "t",
        "101110": "u",
        "101111": "v",
        "110000": "w",
        "110001": "x",
        "110010": "y",
        "110011": "z",
        "110100": "0",
        "110101": "1",
        "110110": "2",
        "110111": "3",
        "111000": "4",
        "111001": "5",
        "111010": "6",
        "111011": "7",
        "111100": "8",
        "111101": "9",
        "111110": "+",
        "111111": "/"
    }
    bn = list(ech.keys())
    vl = list(ech.values())

    ls = []
    en = list(s)
    for i in range((len(en)//2)*2):
        if i%2!=0: continue
        en[i], en[i+1] = en[i+1], en[i]
    s = "".join(en)
    b = list("".join(bn[vl.index(i)] for i in s))
    while (len(b)%8!=0): del b[len(b)-1]
    b = "".join(b)
    for i in range(1,len(b)//8+1):
        ls.append(b[(i*8)-8: i*8])
    return "".join([chr(int(i, 2)) for i in ls])