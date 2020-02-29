c=0
m=int(input("Enter lower limit: "))
n=int(input("Enter upper limit:  "))
for i in range (m,n+1):
    for j in range (2,i):
        if(i%j==0):
            break
    else:
        c+=1
        if c==1:
            print(c,"st prime number in this range is: ",i)
        elif c==2:
            print(c,"nd prime number in this range is: ",i)
        elif c==3:
            print(c,"rd prime number in this range is: ",i)   
        else:
            print(c,"th prime number in this range is: ",i)
            
      
