from selenium import webdriver
import os
from time import sleep


local_path = rf'{os.path.dirname(os.path.realpath(__file__))}\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=local_path)

driver.get('https://www.google.com')
sleep(3)
driver.close()