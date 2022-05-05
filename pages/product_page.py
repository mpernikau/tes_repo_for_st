from .base_page import BasePage
from .locators import ProductPageLocators
import math
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        self.should_be_basket_button()
        self.should_be_promo_url()


    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON)
        assert True

    def should_be_promo_url(self):
        promo_url_check = self.browser.current_url
        assert '?promo=newYear' in promo_url_check
        assert True

    def button_is_clickable(self):
        press_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        press_button.click()
