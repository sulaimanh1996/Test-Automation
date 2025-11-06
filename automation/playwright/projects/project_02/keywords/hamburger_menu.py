# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════

# ════════════════════════ KEYWORDS ════════════════════════
class log_in_process():
    def __init__(self, page):
        self.page = page
    
    def about(self):
        self.page.get_by_role("button", name="Open Menu").click()             
        self.page.get_by_role("link", name="About").click()   

    def log_out(self):
        self.page.get_by_role("button", name="Open Menu").click()             
        self.page.get_by_role("link", name="Logout").click()   

    def all_items(self):
        self.page.get_by_role("button", name="Open Menu").click()             
        self.page.get_by_role("link", name="All Items").click()              
        self.page.get_by_role("button", name="Close Menu").click() 
