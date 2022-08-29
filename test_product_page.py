from pages.product_page import ProductPage
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', urls)
def test_is_user_can_buy_product(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    productP = ProductPage(browser, link)
    productP.openPage()
    productP.IsBuyButtonDisp()
    productP.BuyProductStep()
    productP.solve_quiz_and_get_code()
    productP.CompareProductName()
    productP.ComparePriceOfProductAndTotal()
