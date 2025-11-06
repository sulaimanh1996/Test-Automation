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
def CLICK_ADD_AND_BACK(page, item_id):
    page.click(f"id=item_{item_id}_title_link")
    page.get_by_role("button", name="ADD TO CART").click()
    page.get_by_role("button", name="<- Back").click()

# ? *** Keywords ***
def LOG_IN():
    with sync_playwright() as p:
        # * setup
        browser = p.chromium.launch(headless=False,slow_mo=100)
        context = browser.new_context()
        page = context.new_page()
        page.goto(PAGE_LINK_LOGIN)

        # * error no username (and password)
        page.fill("[id='password']", (INCORRECT_PASSWORD)) 
        page.click("[id='login-button']") 
        assert "Epic sadface: Username is required" in page.content()
        page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "screenshots_1.png"))   

        # * error no password
        page.fill("[id='password']", ("")) 
        page.fill("[id='user-name']", (INCORRECT_USER_NAME)) 
        page.click("[id='login-button']") 
        assert "Epic sadface: Password is required" in page.content()
        page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "screenshots_2.png"))   

        # * error username and password
        page.fill("[id='user-name']", (INCORRECT_USER_NAME)) 
        page.fill("[id='password']", (INCORRECT_PASSWORD)) 
        page.click("[id='login-button']") 
        assert "Epic sadface: Username and password do not match any user in this service" in page.content()
        page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "screenshots_3.png"))   

        # * correct username and password
        page.fill("[id='user-name']", random.choice(CORRECT_USER_NAME)) 
        page.fill("[id='password']", (CORRECT_PASSWORD)) 
        page.click("[id='login-button']") 
        page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "screenshots_4.png"))   

        # * save state
        context.storage_state(path="auth.json")

        # * teardown
        page.close    

def MENU():
    with sync_playwright() as p:
        # * setup with saved state
        browser = p.chromium.launch(headless=False,slow_mo=500)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        page.goto(PAGE_LINK_PRODUCT_PAGE)      

        # * control the "About" link
        page.get_by_role("button", name="Open Menu").click()             
        page.get_by_role("link", name="About").click()   
        page.go_back() 

        # * control the "Logout" link
        page.get_by_role("button", name="Open Menu").click()             
        page.get_by_role("link", name="Logout").click()   
        page.go_back() 

        # * control the "All items" link
        page.get_by_role("button", name="Open Menu").click()             
        page.get_by_role("link", name="All Items").click()              

        # * close button
        page.get_by_role("button", name="Open Menu").click()             
        page.get_by_role("button", name="Close Menu").click() 
    
def PRODUCT_PAGE():
    with sync_playwright() as p:
        # * setup with saved state
        browser = p.chromium.launch(headless=False,slow_mo=500)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        page.goto(PAGE_LINK_PRODUCT_PAGE)

        # * add to cart main product page
        page.click("xpath=//*[@id='inventory_container']/div/div[1]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[2]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[3]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[4]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[5]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[6]/div[3]/button")

        # * remove from cart main product page
        page.click("xpath=//*[@id='inventory_container']/div/div[1]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[2]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[3]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[4]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[5]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[6]/div[3]/button")

        # * click product, add to cart in product page and go back
        CLICK_ADD_AND_BACK(page, "0")
        CLICK_ADD_AND_BACK(page, "1")
        CLICK_ADD_AND_BACK(page, "2")
        CLICK_ADD_AND_BACK(page, "3")
        CLICK_ADD_AND_BACK(page, "4")
        CLICK_ADD_AND_BACK(page, "5")

        # * change order of products
        page.select_option(".product_sort_container", "az")  
        page.select_option(".product_sort_container", "za")  
        page.select_option(".product_sort_container", "lohi")
        page.select_option(".product_sort_container", "hilo")

        # * save state
        context.storage_state(path="auth.json")

        # * teardown
        page.close    

def SHOPPING_CART():
    with sync_playwright() as p:
        # * setup with saved state
        browser = p.chromium.launch(headless=False,slow_mo=500)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        page.goto(PAGE_LINK_PRODUCT_PAGE)
    
        # * add to cart main product page
        page.click("xpath=//*[@id='inventory_container']/div/div[1]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[2]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[3]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[4]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[5]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[6]/div[3]/button")

        # * go to cart
        page.click("a[href='./cart.html']")

        # * remove from cart
        page.click("xpath=//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/button")
        page.click("xpath=//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/button")
        page.click("xpath=//*[@id='cart_contents_container']/div/div[1]/div[5]/div[2]/div[2]/button")
        page.click("xpath=//*[@id='cart_contents_container']/div/div[1]/div[6]/div[2]/div[2]/button")
        page.click("xpath=//*[@id='cart_contents_container']/div/div[1]/div[7]/div[2]/div[2]/button")
        page.click("xpath=//*[@id='cart_contents_container']/div/div[1]/div[8]/div[2]/div[2]/button")

        # * go to cart
        page.click("a[href='./cart.html']")

        # * add to cart main product page
        page.click("xpath=//*[@id='inventory_container']/div/div[1]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[2]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[3]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[4]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[5]/div[3]/button")
        page.click("xpath=//*[@id='inventory_container']/div/div[6]/div[3]/button")

def CHECKOUT():
    with sync_playwright() as p:
        # * setup with saved state
        browser = p.chromium.launch(headless=False,slow_mo=500)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        page.goto(PAGE_LINK_PRODUCT_PAGE)

