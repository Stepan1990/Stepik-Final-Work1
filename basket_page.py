from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "No empty basket message"


    def should_not_be_item_to_buy_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_TO_BUY), "Basket is not empty"
