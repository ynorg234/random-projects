from random import randint as rng
# RNG-26 Encryption Method v0.1
# Made entirely from scratch, using only one package, random.
def encr():
	text = input("Enter text that you want to encrypt here... ")
	key = []
	encrtext = ""
	encstr = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890`~!@#$%^&*()-_=+{[}]|;:?.,<>"
	code = []
	nextletter = ""
	for i in range(len(encstr)):
		nextletter += encstr[rng(0, len(encstr) - 1)]
		if len(nextletter) == 3:
			key.append(nextletter)
			nextletter = ""
	t = 0
	for j in range(len(key)):
		code.append("e"+encstr[j]+" = "+"'"+key[j]+"'")
	for e in range(len(code)):
		exec(code[e], globals())
	z = 0
	while z < len(text)*26:
	    if text[z] == "a":
	        if text[z] == "A":
	            encrtext += eA
	            z += 1
	        else:
	            encrtext += ea
	            z += 1
	    if text[z] == "b":
	        if text[z] == "B":
	            encrtext += eB
	            z += 1
	        else:
	            encrtext += eb
	            z += 1
	    if text[z] == "c":
	        if text[z] == "C":
	            encrtext += eC
	            z += 1
	        else:
	            encrtext += ec
	            z += 1
	    if text[z] == "d":
	        if text[z] == "D":
	            encrtext += eD
	            z += 1
	        else:
	            encrtext += ed
	            z += 1
	    if text[z] == "e":
	        if text[z] == "E":
	            encrtext += eE
	            z += 1
	        else:
	            encrtext += ee
	            z += 1
	    if text[z] == "f":
	        if text[z] == "F":
	            encrtext += eF
	            z += 1
	        else:
	            encrtext += ef
	            z += 1
	    if text[z] == "g":
	        if text[z] == "G":
	            encrtext += eG
	            z += 1
	        else:
	            encrtext += eg
	            z += 1
	    if text[z] == "h":
	        if text[z] == "H":
	            encrtext += eH
	            z += 1
	        else:
	            encrtext += eh
	            z += 1
	    if text[z] == "i":
	        if text[z] == "I":
	            encrtext += eI
	            z += 1
	        else:
	            encrtext += ei
	            z += 1
	    if text[z] == "j":
	        if text[z] == "J":
	            encrtext += eJ
	            z += 1
	        else:
	            encrtext += ej
	            z += 1
	    if text[z] == "k":
	        if text[z] == "K":
	            encrtext += eK
	            z += 1
	        else:
	            encrtext += ek
	            z += 1
	    if text[z] == "l":
	        if text[z] == "L":
	            encrtext += eL
	            z += 1
	        else:
	            encrtext += el
	            z += 1
	    if text[z] == "m":
	        if text[z] == "M":
	            encrtext += eM
	            z += 1
	        else:
	            encrtext += em
	            z += 1
	    if text[z] == "n":
	        if text[z] == "N":
	            encrtext += eN
	            z += 1
	        else:
	            encrtext += en
	            z += 1
	    if text[z] == "o":
	        if text[z] == "O":
	            encrtext += eO
	            z += 1
	        else:
	            encrtext += eo
	            z += 1
	    if text[z] == "p":
	        if text[z] == "P":
	            encrtext += eP
	            z += 1
	        else:
	            encrtext += ep
	            z += 1
	    if text[z] == "q":
	        if text[z] == "Q":
	            encrtext += eQ
	            z += 1
	        else:
	            encrtext += eq
	            z += 1
	    if text[z] == "r":
	        if text[z] == "R":
	            encrtext += eR
	            z += 1
	        else:
	            encrtext += er
	            z += 1
	    if text[z] == "s":
	        if text[z] == "S":
	            encrtext += eS
	            z += 1
	        else:
	            encrtext += es
	            z += 1
	    if text[z] == "t":
	        if text[z] == "T":
	            encrtext += eT
	            z += 1
	        else:
	            encrtext += et
	            z += 1
	    if text[z] == "u":
	        if text[z] == "U":
	            encrtext += eU
	            z += 1
	        else:
	            encrtext += eu
	            z += 1
	    if text[z] == "v":
	        if text[z] == "V":
	            encrtext += eV
	            z += 1
	        else:
	            encrtext += ev
	            z += 1
	    if text[z] == "w":
	        if text[z] == "W":
	            encrtext += eW
	            z += 1
	        else:
	            encrtext += ew
	            z += 1
	    if text[z] == "x":
	        if text[z] == "X":
	            encrtext += eX
	            z += 1
	        else:
	            encrtext += ex
	            z += 1
	    if text[z] == "y":
	        if text[z] == "Y":
	            encrtext += eY
	            z += 1
	        else:
	            encrtext += ey
	            z += 1
	    if text[z] == "z":
	        if text[z] == "Z":
	            encrtext += eZ
	            z += 1
	        else:
	            encrtext += ez
	            z += 1
	print(encrtext)

encr()
