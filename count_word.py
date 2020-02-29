s=input("Enter a sentence: ")
c=0
d=s.lstrip()
for i in d:
    if (i==" "):
        c+=1
print("The number of words are:", c)
    
