from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from time import sleep
load_dotenv()
import os

def login(driver):
  login_button = driver.find_element(By.CSS_SELECTOR, 'a.login.bold')
  login_button.click()
  sleep(3)

  username_field = driver.find_element(By.ID, 'loginFormUser_email')
  password_field = driver.find_element(By.ID, 'loginForm_password')

  username_field.clear()
  username_field.send_keys(os.getenv("user"))
  password_field.clear()
  password_field.send_keys(os.getenv("password"))
  sleep(1)

  driver.execute_script("loginFunctions.submitLogin();")