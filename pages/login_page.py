from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_check = self.browser.current_url
        assert 'login' in url_check
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'No login form'
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'No registration form'
        assert True

    def register_new_user(self, email, password):
        inp_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        inp_email.send_keys(email)
        inp_pass = self.browser.find_element(*LoginPageLocators.PASSWORD)
        inp_pass.send_keys(password)
        inp_confirm_pass = self.browser.find_element(*LoginPageLocators.CONF_PASSWORD)
        inp_confirm_pass.send_keys(password)
        btn_reg = self.browser.find_element(*LoginPageLocators.BTN_REG)
        btn_reg.click()

    def user_login_to_account(self):
        assert self.is_element_present(*LoginPageLocators.LOG_OUT), "User is not logged it"

