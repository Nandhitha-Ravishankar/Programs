# Initializing string
protein = "vlspadkntv"
 
# Character to find
c = "p"
# printing initial string and character
print ("actual protein : ", protein, "\ncharacter_to_find : ", c)
 
# Using Naive Method
res = None
for i in range(0, len(protein)):
    if protein[i] == c:
        res = i + 1
        break
     
if res == None:
    print ("No such character available in string")
else:
    print ("Character {} is present at {} position".format(c, str(res)))