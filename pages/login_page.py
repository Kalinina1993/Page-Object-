from PO.PageObjectPytest.pages.base_page import BasePage
from PO.PageObjectPytest.utils.config import TestData
from PO.PageObjectPytest.utils.locators import LoginPageLocators


class LoginPage(BasePage):
    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions for Login Page"""

    """this is used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this is used to check sign up link"""
    def is_signup_link_exist(self):
        return self.is_visible(LoginPageLocators.LOCATOR_SIGN_IN)

    """this is used to login to app"""
    def do_login(self, username, password):
        self.do_send_keys(LoginPageLocators.LOCATOR_SHOP_REGISTERED_LOGIN, username)
        self.do_send_keys(LoginPageLocators.LOCATOR_SHOP_REGISTERED_PASSWORD, password)
        self.do_click(LoginPageLocators.LOCATOR_SHOP_SUBMIT_BUTTON)









