import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть адресс')
    def go_to_url(self, url):
        return self.driver.get(url)

    @allure.step('Найти локатор на странице')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Нажатие на локатор')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ожидание кликабельности {locator}')
    def find_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step('Получить текст на локаторе')
    def get_text_on_element(self, locator):
        element_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
        return element_text

    @allure.step('Перетащить локатор')
    def drag_and_drop_element(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    @allure.step('Ввести значение в поле')
    def send_keys_to_input(self, locator, keys):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).send_keys(keys)

    @allure.step('Ожидание пока {locator} исчезнет')
    def wait_for_element_go_away(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.none_of(EC.visibility_of_element_located(locator)))

    @allure.step('Пролистать до {locator}')
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element
