from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PO.PageObjectPytest.utils.config import TestData

"""This class is the parent of all pages"""
"""it contains all the generic methods and utilities for all pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        return self.driver.get(TestData.MAIN_PAGE_URL)

    def open_login_page(self):
        return self.driver.get(TestData.BASE_URL)

    def open_cart_page(self):
        return self.driver.get(TestData.CART_PAGE_URL)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def waiting_page(self):
        wait = WebDriverWait(self.driver, 10)
        status = wait.until(EC.url_to_be(TestData.BASE_URL))
        return status

    def waiting_main_page(self):
        wait = WebDriverWait(self.driver, 10)
        status = wait.until(EC.url_to_be(TestData.MAIN_PAGE_URL))
        return status

    def waiting_cart_page(self):
        wait = WebDriverWait(self.driver, 10)
        status = wait.until(EC.url_to_be(TestData.CART_PAGE_URL))
        return status

