from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
driver = webdriver.Remote(options=options)

url = "https://demo.applitools.com/"

driver.get(url)

username = driver.find_element(by=By.ID, value="username")
username.send_keys('Oreoluwa')

password = driver.find_element(by=By.ID, value="password")
password.send_keys('password')

login = driver.find_element(by=By.ID, value="log-in")
login.click()

balance = driver.find_element(by=By.CLASS_NAME, value="balance-value").text
print(balance)

time.sleep(10)