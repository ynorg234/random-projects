from random import randint as rng
# RNG-26 Encryption Method v0.1
# Made entirely from scratch, using only one package, random.
def encr():
	text = input("Enter text that you want to encrypt here... ")
	key = []
	encrtext = ""
	encstr = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890`~!@#$%^&*()-_=+{[}]|;:?.,<>"
	nextletter = ""
	for _ in range(len(encstr)):
		nextletter += encstr[rng(0, len(encstr) - 1)]
		if len(nextletter) == 3:
			key.append(nextletter)
			nextletter = ""
	t = 0
	code = [f"e{encstr[j]} = '{key[j]}'" for j in range(len(key))]
	for item in code:
		exec(item, globals())
	z = 0
	while z < len(text)*26:
		if text[z] == "a":
			encrtext += ea
			z += 1
		if text[z] == "b":
			encrtext += eb
			z += 1
		if text[z] == "c":
			encrtext += ec
			z += 1
		if text[z] == "d":
			encrtext += ed
			z += 1
		if text[z] == "e":
			encrtext += ee
			z += 1
		if text[z] == "f":
			encrtext += ef
			z += 1
		if text[z] == "g":
			encrtext += eg
			z += 1
		if text[z] == "h":
			encrtext += eh
			z += 1
		if text[z] == "i":
			encrtext += ei
			z += 1
		if text[z] == "j":
			encrtext += ej
			z += 1
		if text[z] == "k":
			encrtext += ek
			z += 1
		if text[z] == "l":
			encrtext += el
			z += 1
		if text[z] == "m":
			encrtext += em
			z += 1
		if text[z] == "n":
			encrtext += en
			z += 1
		if text[z] == "o":
			encrtext += eo
			z += 1
		if text[z] == "p":
			encrtext += ep
			z += 1
		if text[z] == "q":
			encrtext += eq
			z += 1
		if text[z] == "r":
			encrtext += er
			z += 1
		if text[z] == "s":
			encrtext += es
			z += 1
		if text[z] == "t":
			encrtext += et
			z += 1
		if text[z] == "u":
			encrtext += eu
			z += 1
		if text[z] == "v":
			encrtext += ev
			z += 1
		if text[z] == "w":
			encrtext += ew
			z += 1
		if text[z] == "x":
			encrtext += ex
			z += 1
		if text[z] == "y":
			encrtext += ey
			z += 1
		if text[z] == "z":
			encrtext += ez
			z += 1
	print(encrtext)

encr()
