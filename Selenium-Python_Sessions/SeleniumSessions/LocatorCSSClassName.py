from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(6)
driver.get("https://www.amazon.in/ap/signin?openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.return_to=https%3A%2F%2Fwww.amazon.in%3A443%2Fap%2Fadam&openid.pape.max_auth_age=900")

# driver.find_element(By.CSS_SELECTOR, '#username').send_keys('sai@gmail.com')
driver.find_element(By.NAME, 'email').send_keys('919866214969')
continues = driver.find_element(By.ID, "continue").click()
passwordd = driver.find_element(By.CLASS_NAME, 'auth-required-field').send_keys('Revanthsai@1')
sign_in = driver.find_element(By.CLASS_NAME, "a-button-input").click()

# driver.find_element(By.CSS_SELECTOR, 'input.a-input-text.a+-span12.auth-autofocus.auth-required-field').send_keys('919866214969')
# driver.find_element(By.XPATH, "//input[@class='a-input-text a-span12 auth-autofocus auth-required-field']").send_keys('919866214969')
# driver.find_element(By.LINK_TEXT,'Create your Amazon account').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,'Amazon account').click()
