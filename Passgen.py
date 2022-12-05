# Requires string, secrets, and pyperclip
import secrets
import string as txt
chrs = txt.ascii_letters + str(1234567890)
def genPass():
    charCount = input("Amount of characters in password... ");
    passW = ''.join(secrets.choice(chrs) for _ in range(int(charCount)))
    print(f'Your password is: {passW}')
genPass()
