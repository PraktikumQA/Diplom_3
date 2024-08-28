import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Нажать на кнопку Конструктор')
    def click_constructor_button(self):
        self.find_element(HomePageLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step('Нажать на кнопку Лента заказов')
    def click_order_feed_button(self):
        self.find_element(HomePageLocators.ORDER_FEED_BUTTON).click()

    @allure.step('Нажать на кнопку Личный Кабинет')
    def click_profile_button(self):
        self.find_element(HomePageLocators.PERSONAL_ACCOUNT).click()

    @allure.step('Кликнуть по кнопке "Войти в аккаунт"')
    def click_login_button(self):
        self.find_element(HomePageLocators.LOGIN_BUTTON).click()

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_make_order(self):
        self.find_element(HomePageLocators.MAKE_ORDER_BUTTON).click()

    @allure.step('Открыть информацию об ингредиенте')
    def open_details(self):
        self.find_element(HomePageLocators.INGREDIENT).click()

    @allure.step('Закрыть информацию об ингредиенте')
    def close_details(self):
        self.find_element(HomePageLocators.DETAILS_CLOSE_BUTTON).click()

    @allure.step('Перенести булку в конструктор')
    def add_ingredient(self):
        source = self.find_element(HomePageLocators.INGREDIENT)
        target = self.find_element(HomePageLocators.INGREDIENT_ADD_SECTION)
        self.drag_and_drop_element(source, target)

    @allure.step('Получить количество ингредиентов')
    def check_amount_ingredients(self):
        return self.find_element(HomePageLocators.INGREDIENT_COUNTER).text

    @allure.step('Подождать пока значек загрузки в окне "Заказ" исчезнет')
    def wait_for_loading_icon_go_away(self):
        self.wait_for_element_go_away(HomePageLocators.LOADING_ICON)

    @allure.step('Подождать загрузки идентификатора заказа и вывести его текст')
    def get_order_id(self):
        return self.find_element(HomePageLocators.ORDER_ID).text

    @allure.step('Закрыть окно созданного заказа')
    def close_new_order(self):
        self.find_element_to_be_clickable(HomePageLocators.CLOSE_ORDER_BUTTON).click()

    @allure.step('Нажать на крестик')
    def click_order_close_button(self):
        self.find_element(HomePageLocators.ORDER_CLOSE_BUTTON).click()

    @allure.step('Получить количество ингредиентов')
    def get_ingredient_counter(self):
        return self.get_text_on_element(HomePageLocators.INGREDIENT_COUNTER)
