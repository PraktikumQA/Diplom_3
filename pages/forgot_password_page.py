import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Подождать загрузки поля "email" и ввести в него {email}')
    def enter_email(self, email):
        self.find_element_to_be_clickable(ForgotPasswordPageLocators.RECOVERY_BUTTON)
        self.find_element(ForgotPasswordPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_recovery_button(self):
        self.find_element_to_be_clickable(ForgotPasswordPageLocators.RECOVERY_BUTTON)
        self.click_element(ForgotPasswordPageLocators.RECOVERY_BUTTON)
