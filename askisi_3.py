#Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες. 												
# Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με μόνο γράμματα και τον κενό χαρακτήρα (space). ✔️
# Χωρείστε αυτό το κείμενο σε λέξεις σύμφωνα με το κενό και ξεκινείστε να αφαιρείτε ζευγάρια λέξεων αν το άθροισμα των γραμμάτων τους είναι 20. ✔️
# Βγάλτε τα στατιστικά για το μήκος των λέξεων που έμειναν, πχ. 10 λέξεις του ενός γράμματος, 12 λέξεις των 2 γραμμάτων, 3 λέξεις των 3 γραμμάτων κτλ.✔️
#Τα ζεύγη δεν χρειάζεται να είναι από συνεχόμενες λέξεις.✔️


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

#Αφαίρεση ζευγαριών με άθροισμα 20 ελέγχοντας όλοι την λίστα (Popping every pair of words whose amount of letters sum up 20)
i = 0
f = 0
while f == 0 & i < len(data):
	j = 0
	f = 0
	while f == 0 & j < len(data):
		if i != j & j < len(data) & i < len(data) & len(data[i]) + len(data[j]) == 20 :
			data.pop(i)
			data.pop(j)
			j = 1
			f = 1
		else:
			j = j + 1
	if f == 0:
		i = i + 1
	else:
		i = 0

#Στατιστικά πλήθους λέξεων για όλα τα πλήθη γραμμάτων ανά λέξη (Word count statistics for all letter crowds per word) 
lwords=[len(i) for i in data]
for i in range(1,max(lwords)):
	print("There are",lwords.count(i),"words with",i,"letters")