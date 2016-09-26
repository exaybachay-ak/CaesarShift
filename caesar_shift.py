#v0.1
#plans for new releases
#1. Create functionality for if user doesn't enter anything
#2. Make an EXE version for compatability
#3. Add XOR and other basic encoding/encryption like vignere

import string
from string import maketrans
#create basic alphabet for reference - input table
intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#change the intab into an array/list
intab = list(intab)
#initialize output table
outtab = []
 
#have user input message to be encrypted, and choose a keylength
bla = raw_input('Enter your unencrypted message here (letters only): ')
key = int(input("Enter your ROT value here, from 1 to 25 (how many characters do you want to rotate your message by?): "))
 
#set variables for output table loop to begin rotating table info
i = 0
restartloop = 25 - key
 
#add alphabet to list, after key
while i <= restartloop:
        #add letters to array, starting from the key forward
        outtab.append(intab[key + i])
        i += 1
 
#add start of alphabet to list, before key
b = 0
while b < key:
        outtab.append(intab[b])
        b += 1
 
#initialize flat strings
outtab1 = ""
intab1 = ""
 
#flatten the list into a single string from each list
x = 0
while x < 26:
        outtab1 += outtab[x]
        intab1 += intab[x]
        x += 1
 
#make uppercase part and concatenate it to lowercase part
intab2 = intab1.upper()
intab3 = intab1 + intab2
outtab2 = outtab1.upper()
outtab3 = outtab1 + outtab2
 
#initialize function to rotate characters
trantab = maketrans(intab3, outtab3)
 
#print encrypted/rotated key, using translation tables
print bla.translate(trantab)
