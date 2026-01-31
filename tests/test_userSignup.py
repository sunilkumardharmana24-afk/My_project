from pages.homePage import SignUp
from pages.scartPage import CartPage
from pages.loginPage import Login
from pages.productPage import Products
from pages.spaymentPage import Payment
from playwright.sync_api import Page, expect
import pytest
import json
from utils.readjson import read_json
file_path = 'testdata/credentials.json'

#Signup user and place an order
@pytest.mark.skip
def test_signup_order(page: Page , sign_up ,login_page , products_page , carts_page , payments_page):
    sign_up.launch_appURL(page)
    testData1 = read_json(file_path)
    sign_up.click_signup(page)
    sign_up.enter_uname_email(page , testData1["email"])
    sign_up.fill_personal_details(page, testData1["password"])
    sign_up.submit_form(page)
    # products_page.add_products_to_cart(page)
    # carts_page.check_out(page)
    # payments_page.order_payment(page)
    # expect(page.get_by_text("Congratulations! Your order has been confirmed!")).to_be_visible()

#Login user and place and order
# @pytest.mark.skip
def test_login_order(page: Page , sign_up ,login_page , products_page , carts_page , payments_page):
    signupPage1 = SignUp(page)
    loginPage1 = Login(page)
    Products1 = Products(page)
    CartPage1 = CartPage(page)
    Payment1 = Payment(page)
    login_page.launch_appURL(page)
    testdata =  read_json('testdata/credentials.json')
    login_page.user_login(page , testdata["email"] , testdata["password"])
    products_page.add_products_to_cart(page)
    carts_page.check_out(page)
    payments_page.order_payment(page)
    print("Order placed successfully")
    expect(page.get_by_text("Congratulations! Your order has been confirmed!")).to_be_visible()