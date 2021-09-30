from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path="E:\\Downloads\\drivers\\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('http://the-internet.herokuapp.com/basic_auth')
# driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
'''In site you have to give username and password
   to skip that step you can follow after//username:password@sitename
   Generally this we can see at Router wifi setup etc 
'''


