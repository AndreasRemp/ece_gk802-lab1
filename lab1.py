import requests
from datetime import datetime ;
a = input("Enter URL: ")
re = requests.get(a)
print("\nHeaders: \n")
for i in re.headers :
    print (i)
print("\nServer: " + re.headers['Server'])
if('Set-Cookie'in re.headers):
    print("\nThe URL Cookies: \n")
    for j in re.cookies:
        print(j.name)
        if j.expires==None:
            print("Does Not Expire\n")
        else:
            ed=float(j.expires)
            nd=datetime.now().timestamp()
            print(" Expires In: ")
            print(datetime.fromtimestamp(ed)-datetime.fromtimestamp(nd))
            print("\n")
else:
    print("No Cookie")
