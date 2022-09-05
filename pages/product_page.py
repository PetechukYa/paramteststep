from selenium.common import ElementNotVisibleException
from selenium.webdriver.common.by import By

from locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def IsBuyButtonDisp(self):
        assert self.is_element_present(*ProductPageLocators.BUY_BUTTON), "Buy button isn present in product page"

    def BuyProductStep(self):
        assert self.is_element_present(*ProductPageLocators.BUY_BUTTON), "Cant find  buy button"
        buttonBuy = self.browser.find_element(By.CSS_SELECTOR, "button[class*='btn-add-to-basket']")
        buttonBuy.click()

    def CompareProductName(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Cant find  product name on page"
        productName = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MASSAGE), "Success massage isnt present"
        succesMassage = self.browser.find_element(*ProductPageLocators.SUCCESS_MASSAGE).text
        assert productName in succesMassage, "Product name isnt contains in success massage"
        print(f"{productName} == {succesMassage}")

    def ComparePriceOfProductAndTotal(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Cant find product price on page"
        productPrice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Basket block isnt displayed"
        basketTotal = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert productPrice in basketTotal, "Price of product isnt equal basket total"

    def should_not_be_success_message_present(self):
        assert self.is_not_present(*ProductPageLocators.SUCCESS_MASSAGE), "Success message isn't presented "

    def should_not_be_success_message_dis(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MASSAGE), "Success message is not disappear after 4 sec"
