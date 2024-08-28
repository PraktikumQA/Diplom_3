from selenium.webdriver.common.by import By


class HomePageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')

    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')

    PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')

    LOGIN_BUTTON = (By.XPATH, './/button[text() = "Войти в аккаунт"]')

    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')

    ORDER_FEED_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')

    MAKE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    INGREDIENT = (By.XPATH, '//p[contains(@class, "BurgerIngredient_ingredient") and text()="Краторная булка N-200i"]')

    INGREDIENT_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')

    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[2]/div[1]/p[contains(@class,"counter_counter")]')

    DETAILS_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_open")]//button[contains(@class, "close")]')

    INGREDIENT_ADD_SECTION = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket__29Cd7")]')

    ORDER_CREATED_WINDOW = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'

    CLOSE_ORDER_BUTTON = By.XPATH, ('//section[contains(@class, "Modal_modal_opened__3ISw4 Modal_modal__P3_V5")]'
                                           '//button[contains(@class, "Modal_modal__close")]')

    LOADING_ICON = (By.XPATH, '//div[contains(@class,"Modal_modal_opened")]')

    ORDER_ID = (By.XPATH, '//h2[contains(@class,"Modal_modal")]')

    ORDER_CLOSE_BUTTON = (By.XPATH, '//section[1]//button')
