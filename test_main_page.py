from .Pages.main_page import MainPage
import pytest
from selenium.webdriver.common.by import By


class TestMainPage():

    def test_guest_can_use_search_form(self, browser):
        link = "https://diia.gov.ua/"
        request = 'реєстрація'
        page = MainPage(browser, link)
        page.open()
        search_page = page.search_info_by_search_form(request)
        search_page.search_result_is_correct()

    @pytest.mark.parametrize('values', ['yerobota', 'pensiyi-pilgi-ta-dopomoga', 'simya', 'licenziyi-ta-dozvoli',
                                        'bezpeka-ta-pravoporyadok', 'transport', 'zemlya-budivnictvo-neruhomist',
                                        'dovidki-ta-vityagi', 'navkolishnye-seredovishche', 'zdorovya', 'dokumenti-ta-gromadyanstvo',
                                        'pidpriyemnictvo'])
    def test_guest_can_go_to_any_services_page(self, browser, values):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.close_cookies_popup()
        service_button = browser.find_element(By.CSS_SELECTOR, f'a.services_item-title[href="/services/categories/gromadyanam/{values}"]')
        page.service_button_lead_to_right_page(service_button, values)



class TestFooterElementsMainPage():

    @pytest.mark.parametrize('items', [str(x) for x in range(1, 13)])
    def test_footer_list_items_active(self, browser, items):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        footer_element = browser.find_element(By.CSS_SELECTOR, f".menu_footer > ul :nth-child({items})")
        page.footer_list_item_is_active(footer_element)


    def test_footer_telegram_button_active(self, browser):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.footer_telegram_button_work_correct()

    def test_footer_instagram_button_active(self, browser):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.footer_instagram_button_work_correct()

    def test_footer_viber_button_active(self, browser):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.footer_viber_button_work_correct()

    def test_footer_facebook_button_active(self, browser):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.footer_facebook_button_work_correct()

    def test_footer_google_play_button_active(self, browser):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.footer_google_play_market_button_work_correct()

    def test_footer_app_store_button_active(self, browser):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.footer_app_store_button_work_correct()

    def test_footer_app_gallery_button_active(self, browser):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.footer_app_gallery_button_work_correct()

    def test_footer_dev_company_gerb_icon_is_visiable(self, browser):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.footer_dev_company_gerb_icon_is_visiable()

    def test_footer_dev_company_diia_icon_is_visiable(self, browser):
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.footer_dev_company_diia_icon_is_visiable()

    def test_footer_dev_company_text_is_visiable(self, browser):
        # links in footer must be visible
        link = "https://diia.gov.ua/"
        page = MainPage(browser, link)
        page.open()
        page.footer_dev_company_text_is_visiable()