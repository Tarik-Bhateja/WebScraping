from selenium import webdriver
from selenium.webdriver.common.by import By   
from selenium.webdriver.support import expected_conditions as EC    
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from ast import Div
import requests 
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=options)
share_name =["tata motors"]
# share_name="mrf"
urls=[]
for share in share_name:
    driver.get("http://groww.in/search?q="+share)
    button = driver.find_element("xpath", '//*[@id="searchPage"]/div[2]/div[2]/div[2]/div')
    # clicking on the button
    # /html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]
    button.click()
    strUrl =driver.current_url
    urls.append(strUrl)
# elem=driver.find_element_by_css_selector("#rso > div > div > div:nth-child(1) > div > div > h3 > a").click()
# url='https://groww.in/stocks/oil-natural-gas-corporation-ltd'


# url=['https://groww.in/stocks/mrf-ltd','https://groww.in/stocks/itc-ltd','https://groww.in/stocks/oil-natural-gas-corporation-ltd']
for link in urls:
    r = requests.get(link)
    htmlContent=r.content
    soup= BeautifulSoup(htmlContent,  'html.parser')
    result=soup.find(class_="exr42mainDiv valign-wrapper").contents[1].get_text()
    print(result)