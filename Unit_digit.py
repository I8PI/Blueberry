a=int(input("Enter digit : "))
p=["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
b=int(a%10)
print("Unit digit is: ",p[b])
c=int((a/10)%10)
print("Ten's digit is: ",p[c])


