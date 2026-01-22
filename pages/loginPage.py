
from playwright.sync_api import Page, expect
import pytest
from pages.homePage import SignUp


class Login(SignUp):

    def __init__(self, page : Page):
        self.page = Page
        self.login_email = page.locator("//input[@data-qa='login-email']")
        self.login_pwd = page.get_by_placeholder("Password")
        self.click_login = page.get_by_role("button", name="Login")


    def user_login(self , page : Page , email , password):
        signupPage1 = SignUp(page)
        signupPage1.launch_appURL(page)
        signupPage1.click_signup(page)
        self.login_email.fill(email)
        self.login_pwd.fill(password)
        self.click_login.click()

