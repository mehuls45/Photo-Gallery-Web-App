import subprocess # subprocess to excute processes and scripts
import webbrowser # to perform operations on browser 
from selenium import webdriver # selenium interacts with webpages, urls, links..
import time 
import urllib # for downloading contents, images from webbrowser using urls


driver = webdriver.Firefox() # make web driver object to perform operations on Mozilla Firefox
driver.get("http://127.0.0.1:8/A") # open browser and enter given url

subprocess.call(['python','C://xampp//htdocs//A//1.pyw'])  # subprocess
subprocess.call(['python','C://xampp//htdocs//A//2.pyw'])

driver.refresh() # Refresh browser
subprocess.call(['python','C://xampp//htdocs//A//trends.py'])
subprocess.call(['python','C://xampp//htdocs//A//matp.py'])
