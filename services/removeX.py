from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

def removeX(wait):
  # Escape x button
  try:
    btn_close = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popupCloseIcon.largeBannerCloser")))
    btn_close.click()
  except NoSuchElementException:
    print("NoSuchElementException")
  except ElementNotInteractableException:
    print('ElementNotInteractableException')