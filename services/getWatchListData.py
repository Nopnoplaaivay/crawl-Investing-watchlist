import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

def getWatchList(driver):

  # Name
  name = driver.find_elements(By.CSS_SELECTOR, '.aqPopupWrapper.js-hover-me-wrapper')
  names = [elem.text for elem in name]

  # Symbol
  symbol = driver.find_elements(By.CSS_SELECTOR, '[data-column-name="symbol"]')
  symbols = [elem.text for elem in symbol][2:]

  # Exchange
  exchange = driver.find_elements(By.CSS_SELECTOR, '[data-column-name="exchange"]')
  exchanges = [elem.text for elem in exchange][2:]

  # Last
  last = driver.find_elements(By.CSS_SELECTOR, '[data-column-name="last"]')
  lasts = [elem.text for elem in last][2:]

  # open
  open_price = driver.find_elements(By.CSS_SELECTOR, '[data-column-name="open"]')
  open_prices = [elem.text for elem in open_price][2:]

  # change percent
  chg_percent = driver.find_elements(By.CSS_SELECTOR, '[data-column-name="chgpercent"]')
  chg_percents = [elem.text for elem in chg_percent][2:]

  # volumn
  vol = driver.find_elements(By.CSS_SELECTOR, '[data-column-name="vol"]')
  vols = [elem.text for elem in vol][2:]

  # time
  time = driver.find_elements(By.CSS_SELECTOR, '[data-column-name="time"]')
  times = [elem.text for elem in time][2:]

  # Save to pandas DataFrame
  columns = ['Ten', 'Ma CK', 'San Giao Dich', 'Close', 'Open', '% Thay doi', 'Khoi luong', 'Thoi gian']
  stock_data = pd.DataFrame(list(zip(names, symbols, exchanges, lasts, open_prices, chg_percents, vols, times)), columns=columns)
  return stock_data