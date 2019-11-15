import random
import string
import time


strlist = []

notdouble = True

def isNotInList(l,s):
    if len(l) == 0:
        return True
    for elem in l:
        if elem == s:
            return False
    return True


start = time.time()
counter = 0
while notdouble:
    instr = "{:}".format(''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8)))
    notdouble = isNotInList(strlist,instr)
    if notdouble:
        strlist.append(instr)
    else:
        break
    counter += 1
    if counter % 10000 == 0:
        print(counter)
        mid = time.time()
        print("{:}s".format(mid-start))
end = time.time()

outfile = open("/home/markus/Desktop/saveStrings.txt",'w')
for line in strlist:
    outfile.write("{:}\n".format(line))
outfile.close()

print("Time: {:}s".format(end-start))
print("Found {:} number of combinations before double.".format(len(strlist)))




