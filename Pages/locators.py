from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, "input.input.form-search_input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn.btn_search-main")
    FOOTER_LIST = (By.CSS_SELECTOR, ".menu_footer > ul :nth-child(1-12)")
    CLOSE_COOKIES_BUTTON = (By.CSS_SELECTOR, 'div.cookies-1_close')

class ServicePageLocators:
    HEADER_OF_SERVICE_PAGE = (By.CSS_SELECTOR, 'h1.article-level-1')


class SearchPageLocators:
    pass


class FooterLocators:
    FACEBOOK_FOOTER_BUTTON = (By.CSS_SELECTOR, '.fa-facebook')
    TELEGRAM_FOOTER_BUTTON = (By.CSS_SELECTOR, '.fa-telegram')
    INSTAGRAM_FOOTER_BUTTON = (By.CSS_SELECTOR, '.fa-instagram')
    VIBER_FOOTER_ICON = (By.CSS_SELECTOR, '.fa-viber')

    GOOGLE_PLAY_FOOTER_BUTTON = (By.CSS_SELECTOR, '.store-google')
    APP_STORE_FOOTER_BUTTON = (By.CSS_SELECTOR, '.store-apple')
    APP_GALLERY_FOOTER_BUTTON = (By.CSS_SELECTOR, '.store-app-gallery')

    DEV_COMPANY_GERB_ICON = (By.CSS_SELECTOR, '.dev-company_icon-gerb')
    DEV_COMPANY_DIIA_ICON = (By.CSS_SELECTOR, '.dev-company_icon-diya')
    DEV_COMPANY_TEXT = (By.CSS_SELECTOR, '.dev-company_text')
