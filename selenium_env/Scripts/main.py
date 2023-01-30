from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)


    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла
