import allure

from locators.home_page_locators import HomePageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Подождать загрузки кнопки "История заказов" и кликнуть на нее')
    def click_history_button(self):
        self.find_element(ProfilePageLocators.ORDER_HISTORY_BUTTON).click()

    @allure.step('Подождать загрузки кнопки "Выход" и кликнуть на нее')
    def click_exit_button(self):
        self.find_element(ProfilePageLocators.EXIT_BUTTON).click()

    @allure.step('Получить ID заказа со страницы истории заказов личного кабинета')
    def get_order_id_history(self):
        return self.find_element(OrderHistoryPageLocators.FIRST_ORDER_IN_ORDER_HISTORY).txt
