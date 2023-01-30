from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
#    browser.implicitly_wait(5)
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '100')
    )
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    browser.execute_script("window.scrollBy(0, 100);")

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла
