from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

city=input("Enter City: ")
browser = webdriver.Chrome()
#browser.implicitly_wait(10)
#city=input("Enter City")
browser.get('https://weather.com/en-IN/')
#wait = WebDriverWait(browser, 10)

#inputElement = wait.until(browser.find_element_by_class_name('theme__inputElement__4bZUj input__inputElement__1GjGE'))
#inputElement = browser.find_element_by_tag_name('input').click()
inputElement =browser.find_elements(By.XPATH, '//*[@id="header-TwcHeader-144269fc-62bc-4d06-bc79-e158594b14ff"]/div/div/div/div[2]/div/div[1]/div/input')
#print(inputElement)
#inputElement =wait.until(browser.find_elements(By.XPATH, '//*[@id="header-TwcHeader-144269fc-62bc-4d06-bc79-e158594b14ff"]/div/div/div/div[2]/div/div[1]/div/input'))
inputElement[0].click()
time.sleep(5)

inputElement[0].send_keys(city)
time.sleep(2)
inputElement[0].send_keys(Keys.ARROW_DOWN)
#inputElement.submit()
inputElement[0].send_keys(Keys.ENTER)

elem = browser.find_elements_by_xpath('//*[@id="hero-left-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b"]/div/div/section/div[3]/table/tbody') # Find the search box
print(elem)
print(type(elem))

for i in range(len(elem)):
   atv=elem[i].text
atv=atv.split("\n")
print(atv)
print(type(atv))
attr1=[]
val1=[]
for p in atv:
   if atv.index(p)%2==0:
      attr1.append(p)
   else:
      val1.append(p)

import pandas
df = pandas.DataFrame(val1,attr1)
df.to_csv("output.csv")	
 




