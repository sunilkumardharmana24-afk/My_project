from playwright.sync_api import Page, expect
import pytest
from utils.readjson import read_json_multiple
file_path1 = 'testdata/multiplecreds.json'
testdata2 = read_json_multiple(file_path1)

@pytest.mark.skip(reason="Skipping multi user login test")
def test_multiuserlogin(page : Page , login_page ,sign_up):
    for key, value in testdata2.items():
        email = value["email"]
        password = value["password"]
        login_page.launch_appURL(page)
        login_page.user_login(page , email , password)  
        expect(page.get_by_text("Logged in as")).to_be_visible()
        sign_up.logout(page)
    # print(testdata2)


@pytest.mark.parametrize("email,password", [(testdata2["login_credentials1"]["email"], testdata2["login_credentials1"]["password"]),
                         (testdata2["login_credentials2"]["email"], testdata2["login_credentials2"]["password"])])
def test_multiuserlogin_alternate(page : Page , login_page ,sign_up , email, password):  
    login_page.launch_appURL(page)
    login_page.user_login(page , email , password)  
    expect(page.get_by_text("Logged in as")).to_be_visible()
    sign_up.logout(page)
    print(f"Testing login for {email} with password {password}")
    
        
     