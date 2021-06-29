from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("http://oyerotech.herokuapp.com/")

link = driver.find_element_by_css_selector("#portfolio > div > div:nth-child(3) > div > a")
link.click()

try:
  element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#portfolio > div > div:nth-child(2) > div:nth-child(1) > div > div > div > div.col-8 > p > a"))
  )
  element.click()
  
  driver.back()
  driver.forward()
  
except:
  print("error")
  driver.quit()

driver.quit()