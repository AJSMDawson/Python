#Password generator with nested functions

import string
import random

lowletters = string.ascii_lowercase
highletters = string.ascii_uppercase
numberchar = string.digits
specialchar = string.punctuation

print('How to Use:')
print('Use the following functions depening upon complexity requirements:')
print('LowChar, LowHighChar, LowHighNum, LowHighNumSpec')
print('Type the length of the password needed in parenthesis')
print('Example: LowHighNumSpec(14) will generate a 14 character password')
#lowercase only
def LowChar(numchar):
    key=''
    for num in range(numchar):
        key+=random.choice(lowletters)
    print (key)
    #return key

#lower and uppercase
def LowHighChar(numchar):
    key=''
    for num in range(numchar):
        key+=random.choice(lowletters + highletters)
    print (key)
    #return key
#lowercase uppercase numbers
def LowHighNum(numchar):
    key=''
    for num in range(numchar):
         key+=random.choice(lowletters + highletters + numberchar)
    print (key)
    #return key
#lowercase uppercase numbers special characters
def LowHighNumSpec(numchar):
    key=''
    for num in range(numchar):
          key+=random.choice(lowletters + highletters + numberchar + specialchar)
    print (key)
    #return key
