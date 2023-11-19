from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
url = "https://web.whatsapp.com/"

driver.get(url)

