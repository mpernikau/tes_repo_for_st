import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.product_page import ProductPage
import time

def test_guest_should_be_on_promo_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_url()
    time.sleep(5)

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.button_is_clickable()
    page.solve_quiz_and_get_code()
    time.sleep(5)

if __name__ == "__main__":
    pytest.main()