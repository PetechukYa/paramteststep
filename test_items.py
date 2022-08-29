from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_is_button_buy_disp(browser):
    browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    sleep(10)
    browser.implicitly_wait(5)
    button = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class*='btn-add-to-basket']")))
    assert button.text is not None, "Текст у кнопки відсутній"
