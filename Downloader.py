import urllib.request
x=input("Enter the source link ") # from where the file is to be downloaded
y=input("Enter the destination address with a backSlash at the end ") # where the file is to be saved
z=input("Enter file name with a fullStop at the end ") # the name by which you wish to save
s=input("Enter extension type ") # the extension of the file
url = x  # from where the file is to be downloaded
urllib.request.urlretrieve(url, str(y)+str(z)+str(s))  # using variables to write the destination 

print('Beginning file download') # ensure success of above code