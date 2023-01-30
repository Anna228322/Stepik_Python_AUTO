from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

link = " http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name.send_keys("a")
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("a")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("a")

    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(os.getcwd() + '/' + 'test.txt')
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()


finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла
