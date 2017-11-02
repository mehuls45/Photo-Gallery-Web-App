import tkinter
import subprocess

from tkinter import *
from distutils.tests import here
import os, subprocess

os.chdir('C://xampp//htdocs//A')

top=Tk()
top.title("Photo Gallery")
keyword =''


def select():
    # insert full function here 
    keyword=Epdf.get()
    print(keyword)
    if os.path.exists('getKey.txt'):
        f = open('getKey.txt','w')
        f.write(keyword)
        f.close()
    top.destroy()
    subprocess.call(['python','C://xampp//htdocs//A//main.py'])
    
TOP_FRAME=Frame(top, width=2000,height=100,bg="powder blue")
TOP_FRAME.pack(side=TOP)
main=Label(TOP_FRAME,font=('default',40,'bold'),text="Twitter Image Extractor",fg='red',anchor='w')
main.grid(row=0,column=0)

Lpdf = Label(top,font=('default',12), text="Enter the keyword to search for images")
Lpdf.pack()
Epdf = Entry(top, bd = 5) 
Epdf.pack()

B = Button(top, text ="Search",command=select)
B.pack()
top.mainloop()


