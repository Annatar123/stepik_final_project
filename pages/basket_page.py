from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Error, the basket is not empty"
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text, "Error, the text is not displayed"

