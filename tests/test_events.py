from pages.events_page import EventsPage

def test_filter_by_date(driver):
    page = EventsPage(driver)

    page.open_page()
    page.filter_by_date()

    cards = page.get_event_cards()

    assert len(cards) > 0


def test_search_events(driver):
    page = EventsPage(driver)

    page.open_page()
    page.search("eco")

    cards = page.get_event_cards()

    assert len(cards) > 0

    for card in cards:
        assert "eco" in card.get_title().lower()