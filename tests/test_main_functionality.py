import allure

from pages.home_page import HomePage
from pages.login_page import LoginPage
from locators.home_page_locators import HomePageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from conftest import driver
from data import ApiUrls, ExistingUser


class TestMainFunctionality:

    @allure.description('Переход по нажатию на «Конструктор»')
    def test_go_to_constructor(self, driver):
        page = HomePage(driver)
        page.go_to_url(ApiUrls.ORDER_FEED)
        page.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE)
        page.click_constructor_button()
        assert page.find_element(HomePageLocators.CONSTRUCTOR_TITLE).text == 'Соберите бургер'

    @allure.description('Переход по нажатию на «Лента заказов»')
    def test_go_to_order_feed(self, driver):
        page = HomePage(driver)
        page.find_element_to_be_clickable(HomePageLocators.CONSTRUCTOR_BUTTON)
        page.click_order_feed_button()
        assert page.find_element(HomePageLocators.ORDER_FEED_TITLE).text == 'Лента заказов'

    @allure.description('Если нажать на ингредиент, появится всплывающее окно с деталями')
    def test_open_ingredient_details(self, driver):
        page = HomePage(driver)
        page.open_details()
        details = page.get_text_on_element(HomePageLocators.INGREDIENT_DETAILS)
        assert details == "Детали ингредиента"

    @allure.description('Всплывающее окно закрывается нажатием по крестику')
    def test_close_ingredient_details(self, driver):
        page = HomePage(driver)

        page.go_to_url(ApiUrls.HOME_URL)
        page.find_element_to_be_clickable(HomePageLocators.INGREDIENT)
        page.open_details()
        page.close_details()
        assert page.find_element(HomePageLocators.INGREDIENT).is_displayed()

    @allure.description('При добавлении ингредиента в заказ, увеличивается счётчик данного ингредиента')
    def test_add_ingredient(self, driver):
        page = HomePage(driver)
        page.add_ingredient()
        quantity = page.check_amount_ingredients()
        assert int(quantity) > 0

    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_make_order_authenticated_user(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.click_login_button()
        login_page.enter_email(ExistingUser.email)
        login_page.enter_password(ExistingUser.password)
        login_page.click_enter_button()
        home_page.add_ingredient()
        home_page.click_make_order()
        assert home_page.find_element(HomePageLocators.ORDER_CREATED_WINDOW).is_displayed()
