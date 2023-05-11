from secrets import choice as sfind
def encr():
	text = input("Enter text to encrypt here... ")
	etext = ""
	stri = "abcdefghijklmnopqrstuvwxyz"
	key = dict()
	for i in range(len(key)):
		key[i] = ''.join(sfind(stri) for j in range(3))
	for k in range(len(text)*26):
		if text[k] == stri[k]:
			etext += key[k]
	return etext
encr()
	
