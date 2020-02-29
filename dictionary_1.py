mydict={"a":25,"b":58,"c":89,"d":27}
valA=" "
for i in mydict:
    if i>valA:
        valA=i
        valB=mydict[i]
print(valA)
print(valB)
print(30 in mydict)
myLst=list(mydict.items())
myLst.sort()
print(myLst[-1])
