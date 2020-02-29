s=input("Enter any string ")
c0=0
c1=0
c2=0
c3=0
for i in range(len(s)):
    if(s[i]>="A" and s[i]<='Z'):
        print(s[i])
        c0=c0+1
    elif(s[i]>='a' and s[i]<='z'):
        print(s[i])
        c1=c1+1
    elif(s[i]>='1' and s[i]<='9'):
        print(s[i])
        c2=c2+1
    else:
        print(s[i])
        c3=c3+1
    print(c0,c1,c2,c3)
