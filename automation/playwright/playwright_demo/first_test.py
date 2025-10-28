from playwright.sync_api import sync_playwright # imports sync_playwright from playwright.sync_api - this runs tests in sync order

def open_browser(): # defines a keyword
    with sync_playwright() as p:    # with starts and stops playwright. p gives acces to browsers
        browser = p.chromium.launch(headless=False) # defines browser and is NOT headless
        page = browser.new_page()   # opens new page
        page.goto("https://google.com") # goes to this page
        print(page.title()) # function print
        browser.close() # closes the browser

open_browser()