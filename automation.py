from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


url = "https://www.merriam-webster.com/"

driver = webdriver.Edge()
driver.get(url)

search = driver.find_element(by=By.ID,  value='search-term')
search.send_keys('Words')

time.sleep()
driver.close()
