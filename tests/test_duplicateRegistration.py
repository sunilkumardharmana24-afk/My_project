
from pages.homePage import SignUp
from utils.readjson import read_json
file_path = 'testdata/credentials.json'
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.skip
def test_duplicate_registration(page : Page , sign_up , login_page):
    sign_up.launch_appURL(page)
    testData1 = read_json(file_path)
    sign_up.click_signup(page)
    sign_up.enter_uname_email(page , testData1["email"])
    sign_up.fill_personal_details(page, testData1["password"]) 
    sign_up.submit_form(page)
    sign_up.logout(page)
    sign_up.click_signup(page)
    sign_up.enter_uname_email(page , testData1["email"])    
    # sign_up.click_signup(page)
    expect(page.get_by_text("Email Address already exist!")).to_be_visible()
    
