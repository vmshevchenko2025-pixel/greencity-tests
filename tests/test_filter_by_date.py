import pytest
from selenium import webdriver
from src.pages.events_page import EventsPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_filter_by_date(driver):
    page = EventsPage(driver)

    page.open()
    page.open_date_filter()
    page.select_date()

    events = page.get_filtered_events()

    assert len(events) > 0