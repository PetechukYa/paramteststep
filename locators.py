from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUY_BUTTON = (By.CSS_SELECTOR, "button[class*='btn-add-to-basket']")
    SUCCES_MASSAGE = (By.CSS_SELECTOR, ".alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class*='product_main']>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class*='product_main']>p[class*='price']")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div[class*='basket']")