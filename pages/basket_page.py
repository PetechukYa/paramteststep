from .base_page import BasePage
from selenium.webdriver.common.by import By
from locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.basket_url_mach()
        self.is_basket_header_mach()

    def basket_url_mach(self):
        assert "basket" in self.browser.current_url, "URL for basket page isnt mach"

    def is_basket_header_mach(self):
        text = self.browser.find_element(*BasketPageLocators.PAGE_HEADER).text
        assert "Basket" in text, f"Page header {text} instead of 'Basket'"

    def is_empty_message_disp(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_PAGE_MESSAGE).text
        assert "Your basket is empty." in text, f"Page message {text} instead of empty basket"

    def basket_has_no_product(self):
        self.is_not_present(*BasketPageLocators.PRODUCT_BLOCK), "Basket not empty"



