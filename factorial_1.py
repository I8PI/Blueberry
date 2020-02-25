from math import fabs , floor
p=1
a=int(floor(fabs(float(input("enter the number: ")))))
while a>0:
    p=p*a
    a=a-1
print(p)
