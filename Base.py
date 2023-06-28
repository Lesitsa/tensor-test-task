from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    def go_to_yandex_site(self):
        with allure.step(f'Переход на сайт: {self.base_url}'):
            return self.driver.get(self.base_url)

    @allure.step("Нахождение элемента по локатору")
    def find_element(self, locator, time=7):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    @allure.step("Нахождение элементов по локатору")
    def find_elements(self, locator, time=7):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    @allure.step("Получение текущего url")
    def url(self):
        return self.driver.current_url

    @allure.step("Получение дескриптора текущего окна")
    def current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Переключение на нужное окно")
    def switch_to_window(self, main_window):
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
