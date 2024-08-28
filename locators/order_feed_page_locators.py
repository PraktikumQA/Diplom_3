from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    ORDER = (By.XPATH, '//li[contains(@class,"OrderHistory_listItem")]')

    CONSIST = (By.XPATH, '//p[contains(@class,"text text_type_main-medium mb-8")]')

    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')

    # Cчетчик "Выполнено за всё время"

    ALL_ORDERS_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    # Cчетчик "Выполнено за сегодня"
    FOR_TODAY_COUNTER = (By.XPATH, '//div[3]/p[contains(@class,"OrderFeed_number")]')

    # Поле "В работе"
    IN_PROGRESS_FIELD = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')

    # Заголовок ленты заказов
    ORDER_FEED_TITLE = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')
