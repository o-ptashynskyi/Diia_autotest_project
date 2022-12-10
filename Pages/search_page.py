from .base_page import BasePage


class SearchResultPage(BasePage):
    def search_result_is_correct(self):
        assert "key=%D1%80%D0%B5%D1%94%D1%81%D1%82%D1%80%D0%B0%D1" in self.browser.current_url, 'search result incorrect'