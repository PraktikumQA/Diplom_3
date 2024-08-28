import allure

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from data import ExistingUser


class TestStellarBurgersPersonalAccount:

    @allure.description('Переход по нажатию на «Личный кабинет»')
    def test_open_personal_account(self, driver):
        page = HomePage(driver)
        page.click_profile_button()
        assert page.find_element(LoginPageLocators.PASSWORD_INPUT).is_displayed()

    @allure.description('Переход в раздел «История заказов»')
    def test_open_history_orders(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        home_page.click_login_button()
        login_page.enter_email(ExistingUser.email)
        login_page.enter_password(ExistingUser.password)
        login_page.click_enter_button()
        home_page.click_profile_button()
        profile_page.click_history_button()
        assert profile_page.find_element(ProfilePageLocators.EXIT_BUTTON).is_displayed()

    @allure.description('Выход из аккаунт')
    def test_logout(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        home_page.click_login_button()
        login_page.enter_email(ExistingUser.email)
        login_page.enter_password(ExistingUser.password)
        login_page.click_enter_button()
        home_page.click_profile_button()
        profile_page.click_exit_button()
        assert login_page.find_element_to_be_clickable(LoginPageLocators.ENTER_BUTTON).is_displayed()
