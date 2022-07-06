# Import Module
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from ast import Div
import requests 
from bs4 import BeautifulSoup

# open Chrome
driver = webdriver.Firefox(executable_path='geckodriver.exe')
# driver.implicitly_wait(2
# driver.maximize_window()
share_name=input()
driver.get("https://www.google.com/search?q=" +share_name + "moneycontrol")
results=driver.find_element(By.CLASS_NAME,'iUh30')

# driver.execute_script("return arguments[0];",results)
results.click()
url=driver.current_url
r = requests.get(url)
htmlContent=r.content
soup= BeautifulSoup(htmlContent,  'html.parser')
result=soup.find(class_="buy_sellper").get_text()
print(result)

driver.close()

