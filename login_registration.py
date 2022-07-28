# import time
# from selenium import webdriver
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# email = driver.find_element_by_id("reg_email")
# email.send_keys("test123@mail.ru")
# password = driver.find_element_by_id("reg_password")
# password.send_keys("123456Sa#$%666")
# reg = driver.find_element_by_name("register")
# reg.click()
# driver.quite()

#2login

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# time.sleep(2)
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("test123@mail.ru")
# password1 = driver.find_element_by_id("password")
# password1.send_keys("123456Sa#$%666")
# log = driver.find_element_by_name("login")
# log.click()
# element_log = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.LINK_TEXT, "Logout"), "Logout"))
# driver.quite()

