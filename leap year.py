while 2>0:
    a=int(input("Enter year: "))
    if (a%100==0 and a%4==0):
        print("The year is a century year and a leap year too")
    elif (a%100!=0 and a%4==0):
        print("The year is a non century year and a leap year")
    else:
        print("The year is not a leap year ")
    print("")    
    print("Author: Somshuvra ")    
