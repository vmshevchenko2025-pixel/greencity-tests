import allure
from src.pages.events_page import EventsPage


@allure.feature("Events")
@allure.story("Search events")
class TestSearchEvents:

    @allure.title("Пошук за ключовим словом повертає результати")
    def test_search_returns_results(self, driver):
        keyword = "eco"
        page = EventsPage(driver)

        with allure.step("Відкрити сторінку подій"):
            page.open()

        with allure.step("Відкрити панель пошуку"):
            page.search_bar.open()

        with allure.step(f"Ввести ключове слово: '{keyword}'"):
            page.search_bar.search(keyword)

        with allure.step("Отримати результати пошуку"):
            events = page.get_events()

        with allure.step("Перевірити: результати не порожні"):
            assert len(events) > 0, f"Пошук за '{keyword}' повинен повертати події"
