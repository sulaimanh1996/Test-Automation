## Keywords
# ? *** Settings ***
import random
import os
from playwright.sync_api import sync_playwright


# ? *** Variables ***
PAGE_LINK_LOGIN=("https://www.saucedemo.com/v1/")
PAGE_LINK_PRODUCT_PAGE=("https://www.saucedemo.com/v1/inventory.html")
CORRECT_USER_NAME=["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
CORRECT_PASSWORD=("secret_sauce")
INCORRECT_USER_NAME=("test")
INCORRECT_PASSWORD=("test")

# ? *** Functions ***


# ? *** Keywords ***
def LOG_IN():
    with sync_playwright() as p:
        # * setup
        browser = p.chromium.launch(headless=False,slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto(PAGE_LINK_LOGIN)

        # * error no username (and password)
        page.fill("[id='password']", (INCORRECT_PASSWORD)) 
        page.click("[id='login-button']") 
        assert "Epic sadface: Username is required" in page.content()
        page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "screenshots.png"))   

        # * error no password
        page.fill("[id='password']", ("")) 
        page.fill("[id='user-name']", (INCORRECT_USER_NAME)) 
        page.click("[id='login-button']") 
        assert "Epic sadface: Password is required" in page.content()
        page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "screenshots.png"))   

        # * error username and password
        page.fill("[id='user-name']", (INCORRECT_USER_NAME)) 
        page.fill("[id='password']", (INCORRECT_PASSWORD)) 
        page.click("[id='login-button']") 
        assert "Epic sadface: Username and password do not match any user in this service" in page.content()
        page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "screenshots.png"))   

        # * correct username and password
        page.fill("[id='user-name']", random.choice(CORRECT_USER_NAME)) 
        page.fill("[id='password']", (CORRECT_PASSWORD)) 
        page.click("[id='login-button']") 
        page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "screenshots.png"))   

        # * save state
        context.storage_state(path="auth.json")

        # * teardown
        page.close    

def PRODUCT_PAGE():
    with sync_playwright() as p:
        # * setup with saved state
        browser = p.chromium.launch(headless=False,slow_mo=500)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        page.goto(PAGE_LINK_PRODUCT_PAGE)

        # * add to cart main product page
        
    