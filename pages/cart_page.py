from PO.PageObjectPytest.pages.base_page import BasePage
from PO.PageObjectPytest.utils.config import TestData
from PO.PageObjectPytest.utils.locators import CartPageLocators, MainPageLocators


class CartPage(BasePage):
    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.CART_PAGE_URL)

    """Page Actions for Cart Page"""

    """this is used to check cart title"""
    def get_cart_page_title(self, title):
        return self.get_title(title)

    """this is used to check cart link"""
    def is_cart_link_exist(self):
        return self.is_visible(CartPageLocators.LOCATOR_SHOP_CART_LINK)

    """this is used to check cart order"""
    def order(self):
        return self.open_main_page(), self.do_click(MainPageLocators.LOCATOR_SHOP_NAVIGATION_TAB_3), \
               self.do_click(CartPageLocators.LOCATOR_SHOP_CART_CHOICE), \
               self.do_click(CartPageLocators.LOCATOR_SHOP_CART_ADD), \
               self.do_click(CartPageLocators.LOCATOR_SHOP_CART_ALERT), self.open_cart_page()

