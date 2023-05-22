from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_BUTTON = (By.XPATH, '//button[@value="Register"]')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.XPATH, '(//div[@class="alertinner "])[1]')
    PRODUCT_NAME = (By.XPATH, '//h1')
    PRODUCT_IN_BASKET_NAME = (By.XPATH, '(//div[@class="alertinner "]/strong)[1]')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    BASKET_TOTAL = (By.XPATH, '//div[@class="alertinner "]/p/strong')


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//div[@id="content_inner"]')
    ITEM_TO_BUY = (By.XPATH, '//h2[@class="col-sm-6 h3"]')
