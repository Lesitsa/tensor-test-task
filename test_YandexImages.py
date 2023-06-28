from YandexImages import YandexImages, YandexImagesLocators
from selenium.webdriver.remote.webelement import WebElement
from loguru import logger

logger.add('test_yandex.log', format='{time} {level} {message}', level='DEBUG', rotation='128 KB',
           compression='zip')


def test_yandex_images(browser):
    logger.debug('---Тест "Картинки в Яндексе"---')
    yandex_main_page = YandexImages(browser)
    yandex_main_page.go_to_yandex_site()
    yandex_services_suggest = yandex_main_page.check_services_suggest()
    condition = isinstance(yandex_services_suggest, WebElement)
    if condition:
        logger.info('Сервисное меню присутствует на странице')
    else:
        logger.error('Сервисное меню отсутсвует на странице')
    assert condition

    yandex_main_page.transition_to_images(yandex_services_suggest)
    current_url = yandex_main_page.url()
    condition = "https://yandex.ru/images/" in current_url
    if condition:
        logger.info('Переход на URL https://yandex.ru/images/ выполнен успешно')
    else:
        logger.error('Ошибка при переходе на URL https://yandex.ru/images/')
    assert condition

    name_of_category = yandex_main_page.open_first_category()
    current_name_of_category = yandex_main_page.current_name_of_category()
    condition = name_of_category == current_name_of_category
    if condition:
        logger.info('Название первой категории отображается в поле поиска')
    else:
        logger.error('Название первой категории не отображается в поле поиска')
    assert condition

    media_viewer, first_image_src = yandex_main_page.open_first_image()
    condition = isinstance(media_viewer, WebElement)
    if condition:
        logger.info('Первая картинка открылась')
    else:
        logger.error('Первая картинка не открылась')
    assert condition

    second_image_src = yandex_main_page.change_image(YandexImagesLocators.LOCATOR_YANDEX_NEXT_BUTTON)
    condition = first_image_src != second_image_src
    if condition:
        logger.info('Картинка сменилась')
    else:
        logger.error('Картинка не сменилась')
    assert condition

    prev_image_src = yandex_main_page.change_image(YandexImagesLocators.LOCATOR_YANDEX_PREV_BUTTON)
    condition = first_image_src == prev_image_src
    if condition:
        logger.info('Успешный возврат к первой картинке')
    else:
        logger.error('Возврат к первой картинке не выполнен')
    assert condition
