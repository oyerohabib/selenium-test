from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
# print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
  main = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "main"))
  )
  
  articles = main.find_elements_by_tag_name("article")
  for article in articles:
    summary = article.find_element_by_class_name("entry-summary")
    print(summary.text)
except:
  print("error")
  driver.quit()

# main = driver.find_element_by_id("main")
# print(driver.page_source)

driver.quit()