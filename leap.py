a=int(input("ENTER YEAR"))
if(a%100==0 and a%400==0): 
    print("leap century year")
elif(a%100!=0 and a%4==0):
    print("leap non century year")

else:
    print("not a leap year")

