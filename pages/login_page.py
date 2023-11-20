from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "There is no authorization form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTRATION), "There is no registration form"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys(password)

        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

