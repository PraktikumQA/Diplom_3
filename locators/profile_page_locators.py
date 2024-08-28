from selenium.webdriver.common.by import By


class ProfilePageLocators:

    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[@href="/account/order-history"]')

    EXIT_BUTTON = (By.XPATH, '//button[contains(@class,"Account_button")]')
