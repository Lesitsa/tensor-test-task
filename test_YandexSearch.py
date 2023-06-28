from YandexSearch import YandexSearch
from selenium.webdriver.remote.webelement import WebElement
from loguru import logger

logger.add('test_yandex.log', format='{time} {level} {message}', level='DEBUG', rotation='128 KB',
           compression='zip')


def test_yandex_search(browser):
    logger.debug('---Тест "Поиск в Яндексе"---')
    yandex_main_page = YandexSearch(browser)
    yandex_main_page.go_to_yandex_site()
    yandex_search_field = yandex_main_page.check_search_field()
    condition = isinstance(yandex_search_field, WebElement)
    if condition:
        logger.info('Поле поиска присутствует на странице')
    else:
        logger.error('Поле поиска отсутствует на странице')
    assert condition

    search_field = yandex_main_page.enter_word("Тензор")
    suggest_elements = yandex_main_page.check_search_suggest()
    condition = len(suggest_elements) > 0
    if condition:
        logger.info('Подсказки поиска появились')
    else:
        logger.error('Подсказки поиска не появились')
    assert condition

    yandex_main_page.press_enter(search_field)
    current_url = yandex_main_page.url()
    condition = "https://yandex.ru/search/" in current_url
    if condition:
        logger.info('Переход на страницу результатов поиска выполнен успешно')
    else:
        logger.error('Ошибка при переходе на страницу результатов поиска')
    assert condition

    result_link = yandex_main_page.search_result_link()
    condition = result_link == "https://tensor.ru/"
    if condition:
        logger.info('Первая ссылка ведет на сайт tensor.ru')
    else:
        logger.error('Первая ссылка не ведет на сайт tensor.ru')
    assert condition
