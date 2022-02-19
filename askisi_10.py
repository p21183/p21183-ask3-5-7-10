#Σας δίνεται αρχείο κειμένου με μόνο ASCII χαρακτήρες. Αρχικά απεικονίστε κάθε χαρακτήρα σε δυαδικό μήκους 7. 
# Από αυτούς κρατάτε μόνο τα πρώτα δύο και τα τελευταία δύο bits. Χωρίστε την ακολουθία σας σε αριθμούς των 16 bits και εμφανίστε τα ακόλουθα στατιστικά: 
# α) Τι ποσοστό είναι ζυγοί;
# β) Τι ποσοστό διαιρείται ακριβώς με το 3;
# γ) Τι ποσοστό διαιρείται ακριβώς με το 5;
# δ) Τι ποσοστό διαιρείται ακριβώς με το 7;

ftxt = open('two_cities_ascii.txt','r')
data = ftxt.read()
ftxt.close()
#Μετατροπή λέξεων σε δυαδικό μήκους 7 (Converting words to 7 digit binary)

import math
import textwrap

def to_bin(x):
  y = []
  z = []
  for i in x:
    y.append(ord(i))
  for i in y:
    z.append(int(bin(i)[2:]))
  return z
bina = to_bin(data)
bina_str = [str(w) for w in bina]
for i in range(0,len(bina_str)):
  if len(bina_str[i]) < 7:
    mis = 7 - len(bina_str[i])
    bina_str[i] = "0" * mis + bina_str[i]

#Κρατάει 4 bit και τα χωρίζει σε αριθμούς των 16 (Keeping the first 2 and last 2 bits and separates them into 16 bit)
for i in range(0,len(bina_str)):
  f2 = bina_str[i][0:2]
  l2 = bina_str[i][5:7]
  b4 = f2 +l2
  bina_str[i] = b4
str = "".join(bina_str)
wrap = textwrap.TextWrapper(width = 16)
l = wrap.wrap(text = str)
for i in range(0,len(l)):
  l[i] = int(l[i])
pos1 = 0
pos2 = 0
pos3 = 0
pos4 = 0

#Εμφανίζει τα ποσοστά (Printing the stats)
for i in range(0,len(l)):
  if l[i] % 2 == 0:
    pos1 += 1
  if l[i] % 3 == 0:
    pos2 += 1
  if l[i] % 5 == 0:
    pos3 += 1
  if l[i] % 7 == 0:
    pos4 += 1

pos1 = (pos1 / len(l)) * 100
pos2 = (pos2 / len(l)) * 100
pos3 = (pos3 / len(l)) * 100
pos4 = (pos4 / len(l)) * 100

print("There are",pos1,"percent even")
print("There are",pos2,"percent multiple of 3")
print("There are",pos3,"percent multiple of 5")
print("There are",pos4,"percent multiple of 7")