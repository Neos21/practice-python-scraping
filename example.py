import time

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options = options)

driver.get('https://www.google.com')
print(f'title is {driver.title}')
time.sleep(3)

driver.quit()
