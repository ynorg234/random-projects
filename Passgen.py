# Requires string, secrets, and pyperclip
import secrets
import string as txt
import pyperclip as clipboard
chrs = txt.ascii_letters + str(1234567890)
def genPass():
  charCount = input("Amount of characters in password...");
  pass = ''.join(secrets.choice(chrs))
  print(f'Your password is: {pass}')
  clipboard.copy(pass)
genPass()
