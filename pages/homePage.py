
from playwright.sync_api import Page, expect
import pytest

class SignUp:
    def __init__(self, page: Page):
        self.page = page
        self.signup_link = page.get_by_role("link", name="Signup / Login")
        self.name_input = page.get_by_role("textbox", name="Name")
        self.email_input = page.locator("input[data-qa='signup-email']")
        self.signup_button = page.get_by_role("button", name="Signup")
        self.mr_radio = page.get_by_role("radio", name="Mr.")
        self.password_input = page.get_by_role("textbox", name="Password *")
        self.days_select = page.locator("#days")
        self.months_select = page.locator("#months")
        self.years_select = page.locator("#years")
        self.newsletter_checkbox = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.offers_checkbox = page.get_by_role("checkbox", name="Receive special offers from")
        self.first_name_input = page.get_by_role("textbox", name="First name *")
        self.last_name_input = page.get_by_role("textbox", name="Last name *")
        self.company_input = page.get_by_role("textbox", name="Company", exact=True)
        self.address1_input = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.address2_input = page.get_by_role("textbox", name="Address 2")
        self.state_input = page.get_by_role("textbox", name="State *")
        self.city_zipcode_input = page.get_by_role("textbox", name="City * Zipcode *")
        self.zipcode_input = page.locator("#zipcode")
        
        self.mobile_number_input = page.get_by_role("textbox", name="Mobile Number *")
        self.create_account_button = page.get_by_role("button", name="Create Account")
        self.click_continue = page.locator("//a[normalize-space()='Continue']")
        self.logout_link = page.get_by_role("link", name="Logout")

        

    def launch_appURL(self, page: Page):
        page.goto("https://automationexercise.com/")
        expect(page).to_have_title("Automation Exercise")
       

    def click_signup(self, page: Page):
        self.signup_link.click()

    def enter_uname_email(self, page: Page, email):
        self.name_input.fill("testuser")
        self.email_input.fill(email)
        self.signup_button.click()

    def fill_personal_details(self, page: Page, password):
        self.mr_radio.check()
        self.password_input.fill(password)
        self.days_select.select_option("10")
        self.months_select.select_option("5")
        self.years_select.select_option("1996")
        self.newsletter_checkbox.check()
        self.offers_checkbox.check()
        self.first_name_input.fill("Test")
        self.last_name_input.fill("User")
        self.company_input.fill("TestCompany")
        self.address1_input.fill("Test Address 1")
        self.address2_input.fill("Test Address 2")
        self.state_input.fill("Test State")
        self.city_zipcode_input.fill("TestCity")
        self.zipcode_input.fill("532421")
        self.mobile_number_input.fill("9989301761")

    def submit_form(self, page: Page):
        self.create_account_button.click()
        expect(page.get_by_text("ACCOUNT CREATED!")).to_be_visible()
        self.click_continue.click()

    def logout(self, page: Page):
        self.logout_link.click()


