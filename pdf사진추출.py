import requests
from PIL import Image
for i in range(2,144): 
    if i < 10:
        r = requests.get("https://ebook.nebooks.co.kr/nw/h/BD05000147/assets/page-images/page-06f09eaa-a1035270-000"+str(i)+".jpg")
        file = open(str(i)+".jpg","wb")
        file.write(r.content)
        file.close()
    elif i >= 10 and i < 100:
        r = requests.get("https://ebook.nebooks.co.kr/nw/h/BD05000147/assets/page-images/page-06f09eaa-a1035270-00"+str(i)+".jpg")
        file = open("9"+str(i)+".jpg","wb")
        file.write(r.content)
        file.close()
    else:
        r = requests.get("https://ebook.nebooks.co.kr/nw/h/BD05000147/assets/page-images/page-06f09eaa-a1035270-0"+str(i)+".jpg")
        file = open("999"+str(i)+".jpg","wb")
        file.write(r.content)
        file.close()
 