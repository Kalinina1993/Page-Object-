from PO.PageObjectPytest.pages.cart_page import CartPage
from PO.PageObjectPytest.tests.test_base import BaseTest
from PO.PageObjectPytest.utils.locators import CartPageLocators


class TestCart(BaseTest):

    def test_cart_link_visible(self):
        self.cartPage = CartPage(self.driver)
        flag = self.cartPage.is_cart_link_exist()
        assert flag

    def test_waiting_main_page(self):
        self.cartPage = CartPage(self.driver)
        status = self.cartPage.waiting_cart_page()
        print(status)
        assert status

    def test_switching_between_pages(self):
        self.cartPage = CartPage(self.driver)
        self.cartPage.open_main_page()
        self.cartPage.open_cart_page()
        text = self.cartPage.get_element_text(CartPageLocators.LOCATOR_SHOP_CART_CONFIRM)
        assert text == "Your shopping cart is empty.", f"Error"

    def test_cart_empty(self):
        self.cartPage = CartPage(self.driver)
        check_element = self.cartPage.get_element_text(CartPageLocators.LOCATOR_SHOP_CART_CONFIRM)
        assert check_element == "Your shopping cart is empty."

    def test_order_in_cart(self):
        self.cartPage = CartPage(self.driver)
        self.cartPage.order()
        check_element = self.cartPage.get_element_text(CartPageLocators.LOCATOR_SHOP_CART_CONFIRM_ORDER)
        assert check_element == "Your shopping cart contains: 1 Product"





