import allure

from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Нажать на кнопку Конструктор')
    def click_constructor_button(self):
        self.find_element(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Подождать загрузки заказа и кликнуть по нему')
    def click_order(self):
        self.find_element(OrderFeedPageLocators.ORDER).click()

    @allure.step("Проверяем изменение каунтера заказов за всё время")
    def get_all_orders_counter_value(self):
        self.find_element(OrderFeedPageLocators.ALL_ORDERS_COUNTER)
        return self.get_text_on_element(OrderFeedPageLocators.ALL_ORDERS_COUNTER)

    @allure.step('Пролистать к счетчику "Выполнено за сегодня" и вывести его текст')
    def scroll_to_for_today_counter_and_get_text(self):
        return self.scroll_to_element(OrderFeedPageLocators.FOR_TODAY_COUNTER).text

    @allure.step('Подождать загрузки заказа в поле "В работе" и вывести его текст')
    def order_in_work_text(self):
        return self.find_element(OrderFeedPageLocators.IN_PROGRESS_FIELD).text
