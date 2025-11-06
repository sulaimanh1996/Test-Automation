# ════════════════════════ SETTINGS ════════════════════════
from keywords import log_in_class
from keywords import hamgurger_menu_class
from keywords import products_class
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
PAGE_URL="https://www.saucedemo.com"
BROWSER_WIDTH=1920
BROWSER_HEIGHT=1080

# ════════════════════════ KEYWORDS ════════════════════════
class setup_class():
    def __init__(self, playwright_instance):
        self.p = playwright_instance

    def setup_browser(self):
        """Setup browser and return page object"""
        browser = self.p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context(viewport={'width': BROWSER_WIDTH,'height': BROWSER_HEIGHT})
        page = context.new_page()
        page.goto(PAGE_URL)
        return browser, page