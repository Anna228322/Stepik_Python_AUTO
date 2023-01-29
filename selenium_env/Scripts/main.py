from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_img_element = browser.find_element(By.CSS_SELECTOR, "img")
    x = x_img_element.get_attribute("valuex")
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
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
