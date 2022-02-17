from PO.PageObjectPytest.pages.main_page import MainPage
from PO.PageObjectPytest.tests.test_base import BaseTest
from PO.PageObjectPytest.utils.locators import MainPageLocators


class TestMain(BaseTest):

    def test_signup_link_visible(self):
        self.mainPage = MainPage(self.driver)
        flag = self.mainPage.is_main_link_exist()
        assert flag

    def test_main_page_title(self):
        self.mainPage = MainPage(self.driver)
        title = self.mainPage.get_title(MainPageLocators.MAIN_PAGE_TITLE)
        assert title == MainPageLocators.MAIN_PAGE_TITLE, f"Error"

    def test_waiting_main_page(self):
        self.mainPage = MainPage(self.driver)
        status = self.mainPage.waiting_main_page()
        print(status)
        assert status

    def test_searching_field(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.enter_word("Dress")
        search_field_button = self.mainPage.is_visible(MainPageLocators.LOCATOR_SHOP_SEARCH_BUTTON)
        assert search_field_button

    def test_navigation_tabs(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.navigation_bar()
        flag = self.mainPage.is_main_link_exist()
        assert flag










