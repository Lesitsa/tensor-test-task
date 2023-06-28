from Base import BasePage
from selenium.webdriver.common.by import By
import time
import allure


class YandexImagesLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SERVICES_SUGGEST = (By.CSS_SELECTOR, ".body_search_yes")
    LOCATOR_YANDEX_FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    LOCATOR_YANDEX_SEARCH_CATEGORY = (By.CLASS_NAME, "input__control")
    LOCATOR_YANDEX_FIRST_IMAGE = (By.CLASS_NAME, "serp-item_pos_0")
    LOCATOR_YANDEX_MEDIA_VIEWER = (By.CLASS_NAME, "MediaViewer")
    LOCATOR_YANDEX_CURRENT_IMAGE = (By.CLASS_NAME, "MMImage-Origin")
    LOCATOR_YANDEX_NEXT_BUTTON = (By.CLASS_NAME, "CircleButton_type_next")
    LOCATOR_YANDEX_PREV_BUTTON = (By.CLASS_NAME, "CircleButton_type_prev")


class YandexImages(BasePage):

    @allure.step("Нахождение сервисного меню")
    def check_services_suggest(self):
        search_field = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        services_suggest = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_SERVICES_SUGGEST)
        return services_suggest

    @allure.step('Переход в "Картинки"')
    def transition_to_images(self, services_suggest):
        main_window = self.current_window_handle()
        services_suggest_all_li = services_suggest.find_element(By.CLASS_NAME, "services-suggest__list-item-more")
        services_suggest_all_a = services_suggest_all_li.find_element(By.CLASS_NAME, "home-link2")
        services_suggest_all_a.click()
        time.sleep(2)

        images = self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Картинки']")
        images.click()
        self.switch_to_window(main_window)

    @allure.step("Открытие первой категории")
    def open_first_category(self):
        first_category = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_CATEGORY)
        name_of_category = first_category.get_attribute("data-grid-text")
        first_category.click()
        time.sleep(2)
        return name_of_category

    @allure.step("Получение названия категории из поля поиска")
    def current_name_of_category(self):
        current_category = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_SEARCH_CATEGORY)
        current_name_of_category = current_category.get_attribute("value")
        return current_name_of_category

    @allure.step("Получение src текущей картинки")
    def current_image_src(self):
        current_image = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_CURRENT_IMAGE)
        current_image_src = current_image.get_attribute("src")
        return current_image_src

    @allure.step("Открытие первой картинки")
    def open_first_image(self):
        first_image = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE)
        first_image.click()
        time.sleep(2)
        media_viewer = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_MEDIA_VIEWER)

        current_image_src = self.current_image_src()
        return media_viewer, current_image_src

    @allure.step("Нажатие кнопки смены картинки и получение ее src")
    def change_image(self, button_locator):
        button = self.find_element(button_locator)
        button.click()
        time.sleep(2)
        current_image_src = self.current_image_src()
        return current_image_src
