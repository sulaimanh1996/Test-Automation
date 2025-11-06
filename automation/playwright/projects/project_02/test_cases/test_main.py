# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright
from keywords import log_in_class, hamgurger_menu_class, products_class, setup_class

# ════════════════════════ TESTCASE ════════════════════════
def test_user_experience():
    with sync_playwright() as p:
        #? SETUP
        setup_handler = setup_class(p)
        browser, page = setup_handler.setup_browser()
        
        #? LOGIN
        login_handler = log_in_class(page)
        login_handler.incorrect_password()
        login_handler.incorrect_username()
        login_handler.incorrect_password_and_username()
        login_handler.correct_password_and_username()

        #? HAMBURGER MENU
        hamburger_handler = hamgurger_menu_class(page)
        hamburger_handler.about()
        page.go_back()
        hamburger_handler.log_out()
        login_handler.correct_password_and_username()
        hamburger_handler.all_items()

        #? PRODUCTS
        product_handler = products_class(page)
        product_handler.add_to_cart_main_page()
        product_handler.remove_from_cart_main_page()
        product_handler.view_products()

        browser.close()
