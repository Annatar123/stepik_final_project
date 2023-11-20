from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')

    NAME_BOOK = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_BOOK = (By.CSS_SELECTOR, '.product_main p.price_color')
    NAME_BOOK_IN_THE_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    PRICE_BOOK_IN_THE_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div .alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

