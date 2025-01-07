# Requires nothing literally
import random
def getPass(length):
    chrs = "qwertyuiopasdfghjklzxcvbnm,<.>/?;:'[}]{=+-_)(*&^%$@!~1234567890"
    return ''.join(random.choice(chrs) for _ in range(length))
length = input("Enter length of password here...")
print(getPass(int(length)))
