a=int(input("Enter digit : "))
p=["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
n=int(input("Enter nth place: "))
c=int((a/(10**n)%10))  
print("nth digit is: ",p[c])


