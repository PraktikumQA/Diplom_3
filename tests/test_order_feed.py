import allure

from data import ApiUrls, ExistingUser
from pages.order_feed_page import OrderFeedPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.home_page_locators import HomePageLocators


class TestStellarBurgersOrderList:
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details(self, driver):
        home_page = HomePage(driver)
        order_feed_page = OrderFeedPage(driver)

        home_page.click_order_feed_button()
        order_feed_page.find_element(HomePageLocators.ORDER_FEED_TITLE)
        order_feed_page.click_order()
        assert order_feed_page.find_element(OrderFeedPageLocators.CONSIST).is_displayed()

    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_all_orders_count(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        home_page.click_login_button()
        login_page.enter_email(ExistingUser.email)
        login_page.enter_password(ExistingUser.password)
        login_page.click_enter_button()

        home_page.click_order_feed_button()
        old_counter = order_feed_page.get_all_orders_counter_value()

        order_feed_page.click_constructor_button()
        home_page.add_ingredient()
        home_page.click_make_order()
        home_page.wait_for_loading_icon_go_away()
        home_page.close_new_order()

        home_page.go_to_url(ApiUrls.ORDER_FEED)
        new_counter = order_feed_page.get_all_orders_counter_value()

        assert new_counter > old_counter

    @allure.description('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_today_order_count(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        home_page.click_login_button()
        login_page.enter_email(ExistingUser.email)
        login_page.enter_password(ExistingUser.password)
        login_page.click_enter_button()

        home_page.click_order_feed_button()
        old_counter = order_feed_page.scroll_to_for_today_counter_and_get_text()

        order_feed_page.click_constructor_button()
        home_page.add_ingredient()
        home_page.click_make_order()
        home_page.wait_for_loading_icon_go_away()
        home_page.close_new_order()

        home_page.go_to_url(ApiUrls.ORDER_FEED)
        new_counter = order_feed_page.scroll_to_for_today_counter_and_get_text()

        assert new_counter > old_counter

    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        home_page.click_login_button()
        login_page.enter_email(ExistingUser.email)
        login_page.enter_password(ExistingUser.password)
        login_page.click_enter_button()

        home_page.add_ingredient()
        home_page.click_make_order()
        home_page.wait_for_loading_icon_go_away()
        order_id = home_page.get_order_id()
        home_page.close_new_order()

        home_page.go_to_url(ApiUrls.ORDER_FEED)
        order_id_in_work = order_feed_page.order_in_work_text()

        assert order_id == order_id_in_work
