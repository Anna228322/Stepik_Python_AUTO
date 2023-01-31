from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import unittest



class test_my_first(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH,
                                      "//label[contains(text(), '*')]//..//input[contains(@class, 'form-control first')]")
        input1.send_keys("test")
        input2 = browser.find_element(By.XPATH,
                                      "//label[contains(text(), '*')]//..//input[contains(@class, 'form-control second')]")
        input2.send_keys("test")
        input3 = browser.find_element(By.XPATH,
                                      "//label[contains(text(), '*')]//..//input[contains(@class, 'form-control third')]")
        input3.send_keys("test@test.test")


        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'not passed')

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//label[contains(text(), '*')]//..//input[contains(@class, 'form-control first')]")
        input1.send_keys("test")
        input2 = browser.find_element(By.XPATH, "//label[contains(text(), '*')]//..//input[contains(@class, 'form-control second')]")
        input2.send_keys("test")
        input3 = browser.find_element(By.XPATH, "//label[contains(text(), '*')]//..//input[contains(@class, 'form-control third')]")
        input3.send_keys("test@test.test")


        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'not passed')


    if __name__ == "__main__":
        unittest.main()


    #с помощью терминала узнаем, какую именно ошибку выводит: (use cmd!!!)((not powershell))
    # python -m unittest {test}.py


