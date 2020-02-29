n=int(input("Enter any nos: "))
for i in range(2,n):
    if(n%i==0):
        break
else:
    print("Its a prime")
