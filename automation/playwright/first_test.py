from playwright.sync_api import sync_playwright

def open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        print(page.title())
        browser.close()

open_browser()