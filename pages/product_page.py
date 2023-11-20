import math
from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def price_and_name_comparison(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK).text == \
               self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_THE_BASKET).text, "Incorrect name book"

        assert self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text == \
               self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_THE_BASKET).text, "Incorrect price book"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Error, success message is displayed"

    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is disappeared, but should not be"
