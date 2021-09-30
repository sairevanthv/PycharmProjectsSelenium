# from selenium import webdriver
# from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome(executable_path="E:\\Downloads\\drivers\\chromedriver.exe")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://www.google.com")
# print(driver.title)

# driver.find_element_by_name("q").send_keys("Naveen Automaitonlabs")
# optionsList = driver.find_elements(By.CSS_SELECTOR,'div.OBMEnb ul li div span')
# print(len(optionsList))

# for ele in optionsList:
#     print(ele.text)
#     if ele.text == "naveen automationlabs youtube":
#         ele.click()
#         break

# print(driver.title)
# time.sleep(5)
# driver.quit()

# Linksinalist.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\\Downloads\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.freshworks.com")
linksList = driver.find_elements(By.TAG_NAME,'a')
print(len(linksList))

# prints texts in terminal

for ele in linksList:
    link_text = ele.text
    print(link_text)

time.sleep(5)
driver.quit()
