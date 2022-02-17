from PO.PageObjectPytest.pages.login_page import LoginPage
from PO.PageObjectPytest.tests.test_base import BaseTest
from PO.PageObjectPytest.utils.config import TestData
from PO.PageObjectPytest.utils.locators import LoginPageLocators


class TestLogin(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(LoginPageLocators.LOGIN_PAGE_TITLE)
        assert title == LoginPageLocators.LOGIN_PAGE_TITLE, f"Error"

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_EMAIL, TestData.PASSWORD)
        text = self.loginPage.get_element_text(LoginPageLocators.LOCATOR_SHOP_CONFIRM_LOGIN_PAGE)
        assert text == "My account", f"Error"

    def test_waiting_login_page(self):
        self.loginPage = LoginPage(self.driver)
        status = self.loginPage.waiting_page()
        print(status)
        assert status

    def test_switching_between_pages(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.open_main_page()
        self.loginPage.open_login_page()
        text = self.loginPage.get_element_text(LoginPageLocators.LOCATOR_SHOP_CONFIRM_LOGIN_PAGE)
        assert text == "My account", f"Error"










