import allure
from src.pages.events_page import EventsPage


@allure.feature("Events")
@allure.story("Filter by date")
class TestFilterByDate:

    @allure.title("Фільтрація подій за датою повертає результати")
    @allure.description(
        "Відкрити сторінку подій, застосувати фільтр за датою "
        "та перевірити, що список подій не порожній."
    )
    def test_filter_by_date_returns_events(self, driver):
        page = EventsPage(driver)

        with allure.step("Відкрити сторінку подій"):
            page.open()

        with allure.step("Відкрити фільтр за датою"):
            page.filter_panel.open_date_filter()

        with allure.step("Вибрати дату в календарі"):
            page.filter_panel.select_date_cell()

        with allure.step("Отримати список подій після фільтрації"):
            events = page.get_events()

        with allure.step("Перевірити: список подій не порожній"):
            assert len(events) > 0, "Після фільтра за датою список не повинен бути порожнім"

    @allure.title("Активний фільтр з'являється після вибору дати")
    def test_active_filter_chip_appears(self, driver):
        page = EventsPage(driver)

        with allure.step("Відкрити сторінку подій"):
            page.open()

        with allure.step("Застосувати фільтр за датою"):
            page.filter_panel.open_date_filter()
            page.filter_panel.select_date_cell()

        with allure.step("Перевірити наявність активного фільтра"):
            active_filters = page.filter_panel.get_active_filters()
            assert len(active_filters) > 0, "Повинен з'явитись тег активного фільтра"
