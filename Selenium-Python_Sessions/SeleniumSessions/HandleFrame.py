from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path="E:\\Downloads\\drivers\\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('http://londonfreelance.org/courses/frames/index.html')

# driver.switch_to.frame(2)  #By index
# driver.switch_to.frame('main')  #frame_element
frame_element = driver.find_element(By.NAME,'main')
driver.switch_to.frame(frame_element)

headerValue = driver.find_element(By.CSS_SELECTOR, 'body h2').text
print(headerValue)

driver.switch_to.default_content()
driver.switch_to.parent_frame()

