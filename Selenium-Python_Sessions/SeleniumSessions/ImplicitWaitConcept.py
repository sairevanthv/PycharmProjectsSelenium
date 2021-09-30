from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="E:\\Downloads\\drivers\\chromedriver.exe")
driver.implicitly_wait(10)
# time out = 10
#dynamic wait
#imp wait will be applied for all theweb elements
#global_wait
#find_element
#find_elements
#only for web elements
#not for non web elements : title, url, alerts


driver.get('https://app.hubspot.com/login')
# driver.get('https://app.hubspot.com/login?__cf_chl_jschl_tk__=pmd_TRxqaUA3WWgmwbqpPrho.nLmVYOm23SjqEgg6rOEmSo-1632567265-0-gqNtZGzNAhCjcnBszQkl')

print(driver.title)

user_name = driver.find_element(By.ID, 'username')
user_name.send_keys('test@gmail.com')

driver.implicitly_wait(5)

driver.find_element(By.ID, 'password').send_keys("test@12345")

# driver.implicitly_wait(0) #nullify of imp wait

# element3
# element4
# element5

