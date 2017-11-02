import urllib.request
import os,shutil

os.chdir('C://xampp//htdocs//A')

saveFile = open('ImageLinks.csv','r')
data = saveFile.read()
data = data.split('\n')

os.chdir('C://xampp//htdocs//A')
shutil.rmtree('C://xampp//htdocs//A//ImageFolder')

os.makedirs('ImageFolder')
os.chdir('C://xampp//htdocs//A//ImageFolder')

for i in range(len(data)-1):
    print(data[i])
    urllib.request.urlretrieve(data[i],"Image_"+str(i+1)+".jpg")
    
 
