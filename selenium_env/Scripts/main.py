from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = " http://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 150);")

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input.send_keys(y)

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()








finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла
