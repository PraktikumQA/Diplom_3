from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    HIDE_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')

    PASSWORD_INPUT_ACTIVE = (By.XPATH, ".//label[@class='input__placeholder text noselect text_type_main-default input__placeholder-focused']")

    RESET_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
