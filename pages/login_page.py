from locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Text Login isnt contains in page url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Cant find login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Cant find reg form"

    def register_new_user(self, email, password):
        self.is_user_name_field_disp()
        self.enter_user_email(email)
        self.is_pass_field_disp()
        self.enter_pass_value(password)
        self.is_pas_conf_field_disp()
        self.enter_pass_conf(password)
        self.click_on_confirm_reg_button()

    def is_user_name_field_disp(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REG_FIELD), "Email field for registration isn't present"

    def enter_user_email(self, mail):
        email_f = self.browser.find_element(*LoginPageLocators.EMAIL_REG_FIELD)
        email_f.send_keys(mail)

    def is_pass_field_disp(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REG_FIELD), \
            "Password field on reg page isnt displayed"

    def enter_pass_value(self, value):
        pass_f = self.browser.find_element(*LoginPageLocators.PASSWORD_REG_FIELD)
        pass_f.send_keys(value)

    def is_pas_conf_field_disp(self):
        assert self.is_element_present(*LoginPageLocators.PASS_CONF_REG_FIELD),\
            "Password field on reg page isnt displayed"

    def enter_pass_conf(self, value):
        pass_f = self.browser.find_element(*LoginPageLocators.PASS_CONF_REG_FIELD)
        pass_f.send_keys(value)

    def click_on_confirm_reg_button(self):
        assert self.is_element_present(*LoginPageLocators.BUTTON_SUBMIT_REG), \
            "Reg confirm button isnt displayed"
        self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT_REG).click()



