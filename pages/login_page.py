import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Подождать загрузки кнопки "Восстановить пароль" и нажать на нее')
    def click_password_recovery_button(self):
        self.find_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON).click()

    @allure.step('Подождать загрузки поля "email" и ввести в него {email}')
    def enter_email(self, email):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step('Подождать загрузки поля "email" и ввести в него {password}')
    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Подождать загрузки кнопки "Войти" и кликнуть на нее')
    def click_enter_button(self):
        self.find_element(LoginPageLocators.ENTER_BUTTON).click()
