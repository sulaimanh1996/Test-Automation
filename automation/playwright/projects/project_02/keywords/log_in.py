# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
INCORRECT_PASSWORD = "wrong_password"
INCORRECT_USER_NAME = "wrong_user"
CORRECT_USER_NAME = "standard_user"
CORRECT_PASSWORD = "secret_sauce"

# ════════════════════════ KEYWORDS ════════════════════════
class log_in_process():
    def __init__(self, page):
        self.page = page
    
    def incorrect_password(self):
        self.page.fill("[id='password']", INCORRECT_PASSWORD) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Username is required" in self.page.content()

    def incorrect_username(self):
        self.page.fill("[id='password']", ("")) 
        self.page.fill("[id='user-name']", (INCORRECT_USER_NAME)) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Password is required" in self.page.content()

    def incorrect_password_and_username(self):
        self.page.fill("[id='user-name']", (INCORRECT_USER_NAME)) 
        self.page.fill("[id='password']", (INCORRECT_PASSWORD)) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Username and password do not match any user in this service" in self.page.content()

    def correct_password_and_username(self):
        self.page.fill("[id='user-name']", (CORRECT_USER_NAME)) 
        self.page.fill("[id='password']", (CORRECT_PASSWORD)) 
        self.page.click("[id='login-button']") 
