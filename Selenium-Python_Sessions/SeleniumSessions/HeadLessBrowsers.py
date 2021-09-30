from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.headless = False
# options.add_argument('--headless')
options.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.implicitly_wait(10)

driver.get('https:amazon.in')
print(driver.title)

time.sleep(5)
driver.quit()