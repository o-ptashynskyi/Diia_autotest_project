import time

from .base_page import BasePage
from .search_page import SearchResultPage
from .locators import MainPageLocators
from .locators import FooterLocators


class MainPage(BasePage):

    def service_button_lead_to_right_page(self, button, param):
        button.click()
        time.sleep(4)
        assert param in self.browser.current_url, 'This is wrong page!'

    def close_cookies_popup(self):
        close_cookies_window_button = self.browser.find_element(*MainPageLocators.CLOSE_COOKIES_BUTTON)
        close_cookies_window_button.click()

    def search_info_by_search_form(self, request_data):
        search_input_field = self.browser.find_element(*MainPageLocators.SEARCH_INPUT_FIELD)
        search_input_field.send_keys(request_data)
        search_button = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()
        return SearchResultPage(browser=self.browser, url=self.browser.current_url)

    def footer_list_item_is_active(self, item):
        assert item != None

    def footer_telegram_button_work_correct(self):
        telegram_button = self.browser.find_element(*FooterLocators.TELEGRAM_FOOTER_BUTTON)
        telegram_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 't.me' in link, 'Telegram button works incorrect!'

    def footer_facebook_button_work_correct(self):
        facebook_button = self.browser.find_element(*FooterLocators.FACEBOOK_FOOTER_BUTTON)
        facebook_button.click()
        time.sleep(5)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(10)
        link = self.browser.current_url
        assert 'facebook' in link, 'Facebook button works incorrect!'

    def footer_instagram_button_work_correct(self):
        instagram_button = self.browser.find_element(*FooterLocators.INSTAGRAM_FOOTER_BUTTON)
        instagram_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 'instagram' in link, 'Instagram button works incorrect!'

    def footer_viber_button_work_correct(self):
        viber_button = self.browser.find_element(*FooterLocators.VIBER_FOOTER_ICON)
        viber_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 'viber' in link, 'Viber button works incorrect!'

    def footer_app_store_button_work_correct(self):
        viber_button = self.browser.find_element(*FooterLocators.APP_STORE_FOOTER_BUTTON)
        viber_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 'apps.apple.com' in link, 'App store button works incorrect!'

    def footer_google_play_market_button_work_correct(self):
        viber_button = self.browser.find_element(*FooterLocators.GOOGLE_PLAY_FOOTER_BUTTON)
        viber_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 'play.google.com' in link, 'Google play button works incorrect!'

    def footer_app_gallery_button_work_correct(self):
        viber_button = self.browser.find_element(*FooterLocators.APP_GALLERY_FOOTER_BUTTON)
        viber_button.click()
        time.sleep(10)
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        time.sleep(5)
        link = self.browser.current_url
        assert 'appgallery.huawei.com' in link, 'App gallery button works incorrect!'

    def footer_dev_company_gerb_icon_is_visiable(self):
        assert self.is_element_visiable(*FooterLocators.DEV_COMPANY_GERB_ICON), 'Dev company gerb icon is not visiable'

    def footer_dev_company_diia_icon_is_visiable(self):
        assert self.is_element_visiable(*FooterLocators.DEV_COMPANY_DIIA_ICON), 'Dev company diia icon is not visiable'

    def footer_dev_company_text_is_visiable(self):
        assert self.is_element_visiable(*FooterLocators.DEV_COMPANY_TEXT), 'Dev company text is not visiable'
