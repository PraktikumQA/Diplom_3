from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_INPUT = (By.XPATH, '//input[@name="name"]')

    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')

    ENTER_BUTTON = (By.XPATH, '//button[contains(@class,"button_button")]')

    PASSWORD_RECOVERY_BUTTON = (By.XPATH, '//a[text() = "Восстановить пароль"]')
