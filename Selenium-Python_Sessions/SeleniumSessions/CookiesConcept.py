from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path="E:\\Downloads\\drivers\\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
print(driver.get_cookies())

driver.add_cookie({"name":"revanthpython","domain":"reddit.com","value":"python"})

cookies = driver.get_cookies()
for cook in cookies:
    print(cook)

