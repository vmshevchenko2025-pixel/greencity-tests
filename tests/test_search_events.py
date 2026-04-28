import pytest
from selenium import webdriver
from src.pages.events_page import EventsPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_events(driver):
    page = EventsPage(driver)

    page.open()
    page.open_search()

    keyword = "eco"
    page.search_by_keyword(keyword)

    results = []
    for _ in range(10):
        results = page.get_search_results()
        if results:
            break

    for event in results:
        assert keyword.lower() in event.text.lower()

        results = page.get_search_results()
        no_results = page.get_no_results_message()

        assert len(results) > 0 or no_results is not None