import re
with open("C:\protocol", "r+") as f:
    protocol="C:\protocol"
    newlist=[]
    for line in protocol:
        line.strip()
        words = line.split()
    for word in words:
        if words not in newlist:
            newlist.append(words)
            newlist.sort()
    print (newlist)
    string=re.split(r'^$[a-z]+^[A-Z]$[a-z]',string)
print (string)
with open("fullforms.txt", "w") as f1:
    for line in f:
        f1.write(string)
        
            

