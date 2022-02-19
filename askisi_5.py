#Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες. 
#Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με μόνο πεζά γράμματα (μετατρέπετε τα κεφαλαία σε πεζά) και τον κενό χαρακτήρα (space).✔️
#Αρχικά, χωρείστε αυτό το κείμενο σε λέξεις σύμφωνα με το κενό. Στις λέξεις που έχετε υπολογίστε τα ακόλουθα στατιστικά: ✔️
#α) ποιες είναι οι δέκα δημοφιλέστερες λέξεις; Αν κάποιες εμφανίζονται το ίδιο πλήθος και βγαίνουν παραπάνω από δέκα, κρατείστε όποιες νομίζετε εσείς ή στην τύχη. ✔️
#β) Ποιοι είναι οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις; ✔️
#γ) Επαναλάβετε το ίδιο για τρία γράμματα. ✔️


#Επεξεργασία κειμένου του αρχείου ώστε να μέινουν μόνο γράμματα και το space (Keeping only letters and the space character)
ftxt= open('two_cities_ascii.txt','r')
data= ftxt.readlines()
filt ='abcdefghijklmnopqrstuvwxyz \nABCDEFGHIJKLMNOPQRSTUVWXYZ'
xchr=[]
for i in range(32,65):
	xchr.append(chr(i))
for i in range(91,97):
	xchr.append(chr(i))
for i in range(123,127):
	xchr.append(chr(i))
xchr.append(chr(10))
data=''.join(data)
for c in xchr:
	data = data.replace(c," ")
data=''.join(filter(filt.__contains__,data))
#Διαχωρισμός κειμένου σε λέξεις ανάλογα με το κενό (Separating the text into words)
data=data.split(' ')

#Μετατροπή όλων των γραμμάτων της λίστας σε πεζά (Convert every letter in lowercase)
data = [i.lower() for i in data]
words=[]

#10 δημοφιλέστερες λέξεις στο κείμενο (10 most popular words in text)
for i in data:
    if i not in words:
        words.append(i)
cwords=[]
for i in words:
	cwords.append(data.count(i))
cwords.pop(9)
words.pop(9)

for i in range(10):
    if i < len(cwords):
        m=cwords.index(max(cwords))
        if i == 0 :
            print("The most popular word is <<",words[m],">> and it appears",max(cwords),"times")
        elif i == 1 :
            print("The 2nd most popular word is <<",words[m],">> and it appears",max(cwords),"times")
        elif i == 2 :
            print("The 3rd most popular word is <<",words[m],">> and it appears",max(cwords),"times")
        else:
            print("The",i+1,"th most popular word is <<",words[m],">> and it appears",max(cwords),"times")
        cwords.pop(m)

#Απλά για καλύτερη διάταξη (For better ordinance)
print()
#3 δημοφιλέστεροι συνδυασμοί δύο πρώτων γραμμάτων (3 most popular two letter combination)
letters2=[]
j = 0
for i in data:
    if len(i) >= 2:
        l = ','.join(i)
        l = l.split(',')
        l = l[0] + l[1]
        letters2.append(l)
#print(letters2,j)
l2 = []
for i in letters2:
    if i not in l2:
        l2.append(i)
cletters2=[]
for i in l2:
	cletters2.append(letters2.count(i))
for i in range(3):
    if i < len(cwords):
        m=cletters2.index(max(cletters2))
        if i == 0 :
            print("The most popular first two letter combination is <<",l2[m],">> and it appears",max(cletters2),"times")
        elif i == 1 :
            print("The 2nd most popular first two letter combination is <<",l2[m],">> and it appears",max(cletters2),"times")
        elif i == 2 :
            print("The 3rd most popular first two letter combination is <<",l2[m],">> and it appears",max(cletters2),"times")
        cletters2.pop(m)

#Απλά για καλύτερη διάταξη (For better ordinance)
print()
#3 δημοφιλέστεροι συνδυασμοί τριών πρώτων γραμμάτων (3 most popular three letter combination)
letters3=[]
for i in data:
    if len(i) >= 3:
        l = ','.join(i)
        l = l.split(',')
        l = l[0] + l[1] + l[2]
        letters3.append(l)
l3 = []
for i in letters3:
    if i not in l3:
        l3.append(i)
cletters3=[]
for i in l3:
	cletters3.append(letters3.count(i))
for i in range(3):
    if i < len(cwords):
        m=cletters3.index(max(cletters3))
        if i == 0 :
            print("The most popular first three letter combination is <<",l3[m],">> and it appears",max(cletters3),"times")
        elif i == 1 :
            print("The 2nd most popular first three letter combination is <<",l3[m],">> and it appears",max(cletters3),"times")
        elif i == 2 :
            print("The 3rd most popular first three letter combination is <<",l3[m],">> and it appears",max(cletters3),"times")
        cletters3.pop(m)