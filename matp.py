import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('C://xampp//htdocs//A')

tweet,count = np.loadtxt("Trends.csv",dtype='str',unpack=True,delimiter=",")

x,y=tweet[0:],count[0:]

y=np.ndarray.astype(y,dtype=int)
l=list(range(len(x)))
plt.axis([0,10,0,90000])
plt.bar(l,y,color='g',label='')
plt.xlabel('Tweet')
plt.ylabel('Tweet Count')

for i in range(0,min(10,len(x))):
    #plt.text(1.2+i,-1 ,x[i])
    plt.text(1+i,-1,x[i])

plt.show()
plt.savefig('World.png')
