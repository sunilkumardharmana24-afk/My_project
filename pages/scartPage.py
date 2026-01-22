from playwright.sync_api import Page, expect
import pytest

class CartPage:

    def __init__(self, page : Page):
        self.page = Page
        self.cart_locator = page.get_by_role("link", name="Cart")
        self.checkout_items = page.locator("//a[text()='Proceed To Checkout']")
        self.add_ordercomments = page.locator(".form-control")
        self.place_order = page.get_by_role("link", name="Place Order")
    
    def check_out(self, page : Page):
        page.wait_for_timeout(5000)
        self.cart_locator.click()
        self.checkout_items.click()
        self.add_ordercomments.fill("Please deliver it asap")
        self.place_order.click()
