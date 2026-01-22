import pytest
from playwright.sync_api import sync_playwright
from pages.homePage import SignUp
from pages.scartPage import CartPage
from pages.loginPage import Login
from pages.productPage import Products
from pages.spaymentPage import Payment

@pytest.fixture(scope = "session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def sign_up(page):
    signupPage1 = SignUp(page)
    return signupPage1

@pytest.fixture(scope="function")
def login_page(page):
    loginPage1 = Login(page)
    return loginPage1

@pytest.fixture(scope="function")
def products_page(page):
    Products1 = Products(page)
    return Products1

@pytest.fixture(scope="function")
def carts_page(page):
    CartPage1 = CartPage(page)
    return CartPage1   

@pytest.fixture(scope="function")
def payments_page(page):
    PaymentsPage1 = Payment(page)
    return PaymentsPage1    
    
    
    
