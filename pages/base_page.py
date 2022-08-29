import selenium
from selenium import webdriver
import selenium
from time import sleep
import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException  # в начале файла


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def openPage(self):
        self.browser.get(self.url)

    def is_element_present(self, by_loc, loc):
        try:
            self.browser.find_element(by_loc, loc)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        sleep(2)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            sleep(2)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
