from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUCKET_BUTTON = (By.CSS_SELECTOR, "div[class*='basket-mini']>span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PAGE_HEADER = (By.CSS_SELECTOR, "div[class='page-header action'] >h1")
    BASKET_PAGE_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCT_BLOCK = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REG_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REG_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_CONF_REG_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_SUBMIT_REG = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    BUY_BUTTON = (By.CSS_SELECTOR, "button[class*='btn-add-to-basket']")
    SUCCESS_MASSAGE = (By.CSS_SELECTOR, ".alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class*='product_main']>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class*='product_main']>p[class*='price']")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div[class*='basket']")
