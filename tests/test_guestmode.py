from pages.homePage import SignUp
from utils.readjson import read_json
from pages.productPage import Products
file_path = 'testdata/credentials.json'
from playwright.sync_api import Page, expect
import pytest

def test_addprodasguest(page : Page , sign_up , login_page , products_page):
    sign_up.launch_appURL(page)
    products_page.add_products_to_cart(page)
    testData1 = read_json(file_path)
    login_page.user_login(page , testData1["email"] , testData1["password"])
    page.screenshot(path="screenshots/guestmode_login.png")

def test_veraddprodasguest(page : Page , sign_up , login_page , products_page):
    sign_up.launch_appURL(page)
    products_page.add_products_to_cart(page)
    testData1 = read_json(file_path)
    login_page.user_login(page , testData1["email"] , testData1["password"])
    expect(page.locator("span#cart-count")).to_have_text("2")
    
    
    
    