import requests
from datetime import datetime ;
a = input("Enter URL: ")
re = requests.get(a)
print("\nHeaders: \n")
for i in re.headers :
    print (i)
