import allure
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Нажать на кнопку показать/скрыть')
    def click_hide_button(self):
        self.find_element(ResetPasswordPageLocators.HIDE_BUTTON).click()
