"""
ID: alex.go2
LANG: PYTHON3
TASK: barn1
"""
f = open("barn1.in", "r")
g = open ("barn1.out", "w")
readfile = f.readlines()
boards = int(readfile[0].split(" ")[0])
numofstalls = int(readfile[0].split(" ")[1])
numofcows = int(readfile[0].split(" ")[2])
delta = 0
cowstalls = []

for x in range(1, numofcows + 1):
    cowstalls.append(int(readfile[x][:-1]))
howmanygroups = 0
whichgroup = 0
def quicksort(arr):
    if len(arr)==0: return []
    if len(arr)==1: return arr
    left = [i for i in arr[1:] if int(i)<int(arr[0])]   
    right = [i for i in arr[1:] if int(i)>=int(arr[0])] 
    return quicksort(left)+[arr[0]]+quicksort(right)
cowstalls = quicksort(cowstalls)

for x in range(1, len(cowstalls)):
    if cowstalls[x] - cowstalls[x - 1] != 1:
        howmanygroups = howmanygroups + 1
cowgroups = [[] for _ in range(howmanygroups + 1)]
cowgroups[0].append(cowstalls[0])
for x in range(1, len(cowstalls)):
    if cowstalls[x] - cowstalls[x - 1] == 1:
        cowgroups[whichgroup].append(cowstalls[x])
    else:
        whichgroup = whichgroup + 1        
        cowgroups[whichgroup].append(cowstalls[x])
whichgroup = 0
if len(cowgroups) > 1:
    smallest = cowgroups[1][0] - cowgroups[0][len(cowgroups[0]) - 1]
delta = len(cowgroups) - boards

while delta > 0:
    whichgroup = 0

    for x in range(0, len(cowgroups) - 1):
        if cowgroups[x + 1][0] - cowgroups[x][len(cowgroups[x]) - 1] < smallest:
            whichgroup = x
            smallest = cowgroups[x + 1][0] - cowgroups[x][len(cowgroups[x]) - 1]
  
    cowgroups[whichgroup] = cowgroups[whichgroup] + cowgroups[whichgroup + 1]
    del cowgroups[whichgroup + 1]
    delta = delta - 1
    if(len(cowgroups) > 1):
        smallest = cowgroups[1][0] - cowgroups[0][len(cowgroups[0]) - 1]

total = 0
for x in range(0, len(cowgroups)):
    total = total + (cowgroups[x][len(cowgroups[x]) - 1] - cowgroups[x][0]) + 1

g.write(str(total) + "\n")
g.close()
    
        
    

        
    
            
            
    
    
    
