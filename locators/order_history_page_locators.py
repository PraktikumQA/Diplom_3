from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:

    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[@href="/account/order-history"]')

    EXIT_BUTTON = (By.XPATH, '//button[contains(@class,"Account_button")]')

    FIRST_ORDER_IN_ORDER_HISTORY = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
