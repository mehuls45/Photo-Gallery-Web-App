import urllib.request
import os,shutil

os.chdir('C://Users//Mehul//Desktop//Pin')

saveFile = open('ImageLinks.csv','r')
data = saveFile.read()

data = data.split('\n')

os.chdir('C://Users//Mehul//Desktop//Pin')
shutil.rmtree('C://Users//Mehul//Desktop//Pin//ImageFolder')

#if not os.path.exists('ImageFolder'):
os.makedirs('ImageFolder')
os.chdir('C://Users//Mehul//Desktop//Pin//ImageFolder')

for i in range(len(data)-1):
    print(data[i])
    urllib.request.urlretrieve(data[i],"Image_"+str(i+1)+".jpg")
    
 
