from PO.PageObjectPytest.pages.base_page import BasePage
from PO.PageObjectPytest.utils.config import TestData
from PO.PageObjectPytest.utils.locators import MainPageLocators


class MainPage(BasePage):
    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.MAIN_PAGE_URL)

    """Page Actions for Main Page"""

    """this is used to get the page title"""
    def get_main_page_title(self, title):
        return self.get_title(title)

    """this is used to check main link"""
    def is_main_link_exist(self):
        return self.is_visible(MainPageLocators.LOCATOR_SHOP_SEARCH_MAIN)

    """this is used to check searching field"""
    def enter_word(self, word):
        self.do_click(MainPageLocators.LOCATOR_SHOP_SEARCH_FIELD)
        self.do_send_keys(MainPageLocators.LOCATOR_SHOP_SEARCH_FIELD, word)
        self.do_click(MainPageLocators.LOCATOR_SHOP_SEARCH_BUTTON)

    """this is used to check navigation bar of main page"""
    def navigation_bar(self):
        return self.do_click(MainPageLocators.LOCATOR_SHOP_NAVIGATION_TAB_1), self.open_main_page(), \
               self.do_click(MainPageLocators.LOCATOR_SHOP_NAVIGATION_TAB_2), self.open_main_page(), \
               self.do_click(MainPageLocators.LOCATOR_SHOP_NAVIGATION_TAB_3), self.open_main_page(), \
               self.do_click(MainPageLocators.LOCATOR_SHOP_NAVIGATION_TAB_4), self.open_main_page(), \
               self.do_click(MainPageLocators.LOCATOR_SHOP_NAVIGATION_TAB_5), self.open_main_page()






