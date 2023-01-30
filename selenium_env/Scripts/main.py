from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    sum = int(num1) + int(num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла
