from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()


    def should_be_added_item_in_basket(self):
        added_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME)
        assert added_product.text == product_in_basket.text, "Chosen product has not been added to basket"
    def should_be_basket_total_equal_item_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert product_price.text == basket_total.text, "Item price is not equal to basket total"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is displayed, but should not"

