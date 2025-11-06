# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
INCORRECT_USERNAME = "wrong_user"
INCORRECT_PASSWORD = "wrong_password"
CORRECT_USERNAME= "standard_user"
CORRECT_PASSWORD= "secret_sauce"

# ════════════════════════ KEYWORDS ════════════════════════
class log_in_class():
    def __init__(self, page):
        self.page = page
    
    def incorrect_password(self):
        self.page.fill("[id='password']", INCORRECT_PASSWORD) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Username is required" in self.page.content()

    def incorrect_username(self):
        self.page.fill("[id='password']", ("")) 
        self.page.fill("[id='user-name']", INCORRECT_USERNAME) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Password is required" in self.page.content()

    def incorrect_password_and_username(self):
        self.page.fill("[id='user-name']", INCORRECT_USERNAME) 
        self.page.fill("[id='password']", INCORRECT_PASSWORD) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Username and password do not match any user in this service" in self.page.content()

    def correct_password_and_username(self):
        self.page.fill("[id='user-name']", CORRECT_USERNAME) 
        self.page.fill("[id='password']", CORRECT_PASSWORD) 
        self.page.click("[id='login-button']") 
