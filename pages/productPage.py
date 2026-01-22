from playwright.sync_api import Page, expect
import pytest



class Products:

    def __init__(self , page : Page):
        self.click_products = page.locator("//a[@href='/products']")
        self.view_bluetop = page.locator("a[href='/product_details/1']")
        self.add_to_cart = page.get_by_role("button", name="Add to cart")
        self.continue_shopping = page.get_by_role("button", name="Continue Shopping")
        self.view_tshirt = page.locator("a[href='/product_details/2']")
        
        

    def add_products_to_cart(self , page : Page):
        self.click_products.click()
        self.view_bluetop.click()
        self.add_to_cart.click()
        self.continue_shopping.click()
        self.click_products.click()
        self.view_tshirt.click()
        self.add_to_cart.click()
        self.continue_shopping.click()