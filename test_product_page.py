import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
product_link_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


@pytest.mark.user_register
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """"
        Открыть страницу регистрации;
        Зарегистрировать нового пользователя;
        Проверить, что пользователь авторизован
        """""
        page = LoginPage(browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "TestPassword_01"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """"
        Выполнить шаги из setup;
        Открыть страницу товара (промо);
        Добавить товар в корзину;
        Решить квиз в алерте;
        Проверить, что в корзине выбранный товар;
        Проверить, что цена товара совпадает с суммой корзины
        """""
        page = ProductPage(browser, product_link_promo)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_added_item_in_basket()
        page.should_be_basket_total_equal_item_price()
        time.sleep(1)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link, 0)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    """"
    Открыть страницу товара (промо);
    Добавить товар в корзину;
    Решить квиз в алерте;
    Проверить, что в корзине выбранный товар;
    Проверить, что цена товара совпадает с суммой корзины
    """""
    page = ProductPage(browser, product_link_promo)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_item_in_basket()
    page.should_be_basket_total_equal_item_price()

@pytest.mark.xfail(reason="отрицательная проверка")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link, 0)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link, 0)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="отрицательная проверка")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link, 0)
    page.open()
    page.add_to_basket()
    page.should_success_message_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """"
    Открыть страницу товара;
    Перейти на страницу логина;
    Проверить корректность отображения страницы логина:
    - ссылка содержит "login"
    - форма регистрации присутствует на странице
    - форма авторизации присутствует на странице
    """""
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """"
    Открыть страницу товара;
    Перейти в Корзину;
    Проверить, что в корзине нет товаров;
    Проверить, что отображается сообщение о пустой корзине
    """""
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_item_to_buy_in_basket()
    basket_page.should_be_empty_basket_message()







