from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUCKET_BUTTON = (By.CSS_SELECTOR, "div[class*='basket-mini']>span>a")


class MainPageLocators:
    L = (By.CSS_SELECTOR, "awdawdawd")


class BasketPageLocators:
    PAGE_HEADER = (By.CSS_SELECTOR, "div[class='page-header action'] >h1")
    BASKET_PAGE_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCT_BLOCK = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUY_BUTTON = (By.CSS_SELECTOR, "button[class*='btn-add-to-basket']")
    SUCCESS_MASSAGE = (By.CSS_SELECTOR, ".alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class*='product_main']>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class*='product_main']>p[class*='price']")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div[class*='basket']")
