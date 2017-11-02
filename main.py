import subprocess, webbrowser
from selenium import webdriver
import time
import urllib


driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8/A")

subprocess.call(['python','C://xampp//htdocs//A//1.pyw'])
subprocess.call(['python','C://xampp//htdocs//A//2.pyw'])

driver.refresh()
subprocess.call(['python','C://xampp//htdocs//A//trends.py'])
subprocess.call(['python','C://xampp//htdocs//A//matp.py'])
