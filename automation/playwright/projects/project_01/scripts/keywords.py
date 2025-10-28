import re
from playwright.sync_api import sync_playwright

username = "standard_user"
password = "secret_sauce"
AUTH_FILE = "auth.json"  


def click_and_back(page, product_name: str):
    page.get_by_role("link", name=product_name).click()
    page.get_by_role("button", name="<- Back").click()


def log_in():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.saucedemo.com/v1/")

        page.click("[id='login-button']")
        assert page.locator("text=Epic sadface: Username is required").is_visible()

        page.fill("input[id='user-name']", "test")
        page.click("[id='login-button']")
        assert page.locator("text=Epic sadface: Password is required").is_visible()

        page.fill("input[id='password']", "test")
        page.click("[id='login-button']")
        assert page.locator(
            "text=Epic sadface: Username and password do not match any user in this service"
        ).is_visible()

        page.fill("input[id='user-name']", username)
        page.fill("input[id='password']", password)
        page.click("[id='login-button']")

        context.storage_state(path=AUTH_FILE)

        context.close()
        browser.close()


def products():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)

        context = browser.new_context(storage_state=AUTH_FILE)
        page = context.new_page()

        page.goto("https://www.saucedemo.com/v1/inventory.html")
        click_and_back(page, "Sauce Labs Backpack")
        click_and_back(page, "Sauce Labs Bolt T-Shirt")
        click_and_back(page, "Sauce Labs Onesie")
        click_and_back(page, "Sauce Labs Bike Light")
        click_and_back(page, "Sauce Labs Fleece Jacket")
        click_and_back(page, "Test.allTheThings() T-Shirt (")

        page.locator("div").filter(
            has_text=re.compile(r"^\$29\.99ADD TO CART$")
        ).get_by_role("button").click()
        page.get_by_role("button", name="REMOVE").click()
        page.locator("div:nth-child(3) > .pricebar > .btn_primary").click()
        page.get_by_role("button", name="REMOVE").click()
        page.locator("div").filter(
            has_text=re.compile(r"^\$7\.99ADD TO CART$")
        ).get_by_role("button").click()
        page.get_by_role("button", name="REMOVE").click()
        page.locator("div").filter(
            has_text=re.compile(r"^\$9\.99ADD TO CART$")
        ).get_by_role("button").click()
        page.get_by_role("button", name="REMOVE").click()
        page.locator("div").filter(
            has_text=re.compile(r"^\$49\.99ADD TO CART$")
        ).get_by_role("button").click()
        page.get_by_role("button", name="REMOVE").click()
        page.locator("div:nth-child(6) > .pricebar > .btn_primary").click()
        page.get_by_role("button", name="REMOVE").click()

        context.close()
        browser.close()
