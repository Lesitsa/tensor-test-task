from Base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import allure


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_SUGGEST = (By.CLASS_NAME, "mini-suggest__item")
    LOCATOR_YANDEX_RESULTS = (By.CLASS_NAME, "serp-item")


class YandexSearch(BasePage):

    @allure.step("Нахождение поля поиска")
    def check_search_field(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    def enter_word(self, word):
        with allure.step(f'Ввод слова "{word}" в поле поиска'):
            search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
            search_field.click()
            search_field.send_keys(word)
            return search_field

    @allure.step("Нахождение элементов таблицы поиска с подсказками")
    def check_search_suggest(self):
        return self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_SUGGEST)

    @allure.step("Нажатие ENTER")
    def press_enter(self, search_field):
        search_field.send_keys(Keys.ENTER)

    @allure.step("Получение 1ой ссылки результатов поиска")
    def search_result_link(self):
        search_results = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_RESULTS)
        result3 = search_results[0]\
            .find_element(By.CLASS_NAME, "Organic")\
            .find_element(By.CLASS_NAME, "OrganicTitle") \
            .find_element(By.CLASS_NAME, "Link")

        result_link = result3.get_attribute("href")
        return result_link
