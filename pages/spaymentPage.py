from playwright.sync_api import Page, expect
import pytest


class Payment:

    def __init__(self , page : Page):
        self.page = Page
        self.cardholder_name = page.locator("//input[@name='name_on_card']")
        self.card_number = page.locator("//input[@name='card_number']")
        self.cvv = page.locator("//input[@placeholder='ex. 311']")
        self.exp_month = page.locator("//input[@placeholder='MM']")
        self.exp_year = page.locator("//input[@placeholder='YYYY']")  
        self.pay_order = page.locator("#submit")
    
    def order_payment(self , page : Page):
        self.cardholder_name.fill("Sunil")
        self.card_number.fill("537341989387")
        self.cvv.fill("123")
        self.exp_month.fill("10")
        self.exp_year.fill("2030")
        self.pay_order.click()