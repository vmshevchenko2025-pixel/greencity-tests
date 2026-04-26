from components.base_component import BaseComponent


class EventCardComponent(BaseComponent):

    def title(self):
        return self.find(".event-title").text

    def date(self):
        return self.find(".event-date").text