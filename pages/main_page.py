from pages.base_page import BasePage
from pages.login_page import LoginPage
from locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        log_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        log_link.click()
    #    return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link isnt present"