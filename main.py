import string
import secrets

specialChars = string.punctuation
digits = string.digits
lettersUpper = string.ascii_uppercase
lettersLower = string.ascii_lowercase
chars = lettersUpper + lettersLower + digits + specialChars

pwdLen = 12 #int(input("Enter password length: "))

#At least conditions:

numUppers = 0
numDigits = 0
numSpecials = 1


#Generate required characters
conditionChars = ''

for i in range(numUppers):
  conditionChars += ''.join(secrets.choice(lettersUpper))
for i in range(numDigits):
  conditionChars += ''.join(secrets.choice(digits))
for i in range(numSpecials):
  conditionChars += ''.join(secrets.choice(specialChars))

#update password length
pwdLen -= numUppers + numDigits + numSpecials

pwdTemp = conditionChars + ''

for i in range(pwdLen):
  pwdTemp += ''.join(secrets.choice(chars))

#shuffle password (otherwise condition-generated characters are always at start of password)
#Fisher-Yates Algorithm (to avoid using random module)
#start with last element and swap it with a randomly selected element

def FisherYates(pwdToShuffle):
  pwdList = pwdToShuffle.split()
  for i in range((len(pwdList)-1), 0, -1):
    j = secrets.randbelow(i+1)
    pwdList[i], pwdList[j] = pwd[j], pwd[i]
  pwd = ''.join(pwdList)
  return pwd

pwd = FisherYates(pwdTemp)
print(pwd)
  
