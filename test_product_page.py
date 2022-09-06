from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest
import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', urls)
def test_is_user_can_buy_product(browser, link):
    productP = ProductPage(browser, link)
    productP.openPage()
    productP.IsBuyButtonDisp()
    productP.BuyProductStep()
    productP.solve_quiz_and_get_code()
    productP.CompareProductName()
    productP.ComparePriceOfProductAndTotal()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    productPage = ProductPage(browser, product_base_link)
    productPage.openPage()
    productPage.IsBuyButtonDisp()
    productPage.BuyProductStep()
    productPage.should_not_be_success_message_present()


def test_guest_cant_see_success_message(browser):
    product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    productPage = ProductPage(browser, product_base_link)
    productPage.openPage()
    productPage.should_not_be_success_message_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    productPage = ProductPage(browser, product_base_link)
    productPage.openPage()
    productPage.IsBuyButtonDisp()
    productPage.BuyProductStep()
    productPage.should_not_be_success_message_dis()


@pytest.mark.login
class TestLoginFunc:

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.openPage()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.openPage()
    page.basket_button_present()
    page.go_to_basket_page()
    basketPage = BasketPage(browser, browser.current_url)
    basketPage.should_be_basket_page()
    basketPage.basket_has_no_product()
    basketPage.is_empty_message_disp()


@pytest.mark.new
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        log_page = LoginPage(browser, link)
        log_page.openPage()
        email = str(time.time()) + "@mailinator.com"
        password = "nevelada13"
        log_page.register_new_user(email, password)
        log_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, product_base_link)
        product_page.openPage()
        product_page.should_not_be_success_message_present()


@pytest.mark.need_review
class TestNeededReviewTests:
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_p = ProductPage(browser, link)
        product_p.openPage()
        product_p.IsBuyButtonDisp()
        product_p.BuyProductStep()
        product_p.CompareProductName()
        product_p.ComparePriceOfProductAndTotal()

    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_p = ProductPage(browser, link)
        product_p.openPage()
        product_p.IsBuyButtonDisp()
        product_p.BuyProductStep()
        product_p.CompareProductName()
        product_p.ComparePriceOfProductAndTotal()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.openPage()
        page.basket_button_present()
        page.go_to_basket_page()
        basketPage = BasketPage(browser, browser.current_url)
        basketPage.should_be_basket_page()
        basketPage.basket_has_no_product()
        basketPage.is_empty_message_disp()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.openPage()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
