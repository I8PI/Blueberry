n=input("enter the number: ")
a=int(n)
l=len(n)
rev=0
while l>0:
  dig=a%10
  rev=rev*10+dig
  a=a//10
  l=l-1
print("the reverse digit is ",rev, sep="--> " ) 
