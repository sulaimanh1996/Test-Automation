# ════════════════════════ SETTINGS ════════════════════════
from keywords import log_in_process
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
PAGE_LINK_LOGIN=("https://www.saucedemo.com")

# ════════════════════════ TESTCASE ════════════════════════
def test_log_in():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()
        page.goto(PAGE_LINK_LOGIN)
        
        login_handler = log_in_process(page)
        
        login_handler.incorrect_password()
        login_handler.incorrect_username()
        login_handler.incorrect_password_and_username()
        login_handler.correct_password_and_username()
        
        browser.close()