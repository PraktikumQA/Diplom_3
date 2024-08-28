import allure

from data import ApiUrls, ExistingUser
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_password_recovery_open(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        home_page.click_login_button()
        login_page.click_password_recovery_button()
        assert forgot_password_page.find_element(ForgotPasswordPageLocators.TITLE_RECOVERY).is_displayed()

    @allure.description('Ввод почты и нажатие на кнопку «Восстановить»')
    def test_password_recovery_email(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        home_page.go_to_url(ApiUrls.LOGIN)
        login_page.scroll_to_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        login_page.click_password_recovery_button()
        forgot_password_page.enter_email(ExistingUser.email)
        forgot_password_page.click_recovery_button()
        assert reset_password_page.find_element(ResetPasswordPageLocators.RESET_TITLE)

    @allure.description('Нажатие на кнопку показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_input_active(self, driver):
        home_page = HomePage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        home_page.click_login_button()
        login_page = LoginPage(driver)
        login_page.click_password_recovery_button()
        forgot_password_page.enter_email(ExistingUser.email)
        forgot_password_page.click_recovery_button()
        reset_password_page.click_hide_button()
        assert reset_password_page.find_element(ResetPasswordPageLocators.PASSWORD_INPUT_ACTIVE).is_displayed()
