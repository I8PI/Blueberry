st1=input("enter a string ")
st3=st1.lower()
stv={'a','e','i','o','u'}
for x in st3 and stv:
    print(x)
    st3=st3.replace(x," ")
print(st1,"::with vowels")
print(st3,"::without vowels")    
