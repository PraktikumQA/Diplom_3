from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name']")

    RECOVERY_BUTTON = (By.XPATH, '//button[text() = "Восстановить"]')

    TITLE_RECOVERY = (By.XPATH, "//h2[text()='Восстановление пароля']")
