import urllib.request
import os,shutil  # shutil is to remove entire directory

os.chdir('C://xampp//htdocs//A')

saveFile = open('ImageLinks.csv','r') # open link file
data = saveFile.read() # read from file
data = data.split('\n') # split by new line, so that each link will be stored in the list

os.chdir('C://xampp//htdocs//A')  
shutil.rmtree('C://xampp//htdocs//A//ImageFolder')  # delete old image folder.

os.makedirs('ImageFolder') # make new folder to save new images
os.chdir('C://xampp//htdocs//A//ImageFolder')

for i in range(len(data)-1):
    print(data[i]) # print image url
    urllib.request.urlretrieve(data[i],"Image_"+str(i+1)+".jpg") # download and save image in Image folder, sequentially..
    # request to retieve images.
     
