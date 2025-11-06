# 🔑 KEYWORD CLASS TEMPLATES
Copy-paste templates based on PROJECT_02 structure with improved patterns

## 📋 **TEMPLATE OVERVIEW**
Ready-to-use class templates for common automation scenarios.

---

## ⭐ **SETUP CLASS TEMPLATE (NEW PATTERN)**

### **File: `keywords/setup.py`**
```python
# ════════════════════════ SETTINGS ════════════════════════
from keywords import log_in_class
from keywords import hamgurger_menu_class
from keywords import products_class
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
PAGE_URL = "https://www.saucedemo.com"  # Replace with your app URL
BROWSER_WIDTH = 1920
BROWSER_HEIGHT = 1080

# ════════════════════════ KEYWORDS ════════════════════════
class setup_class():
    def __init__(self, playwright_instance):
        self.p = playwright_instance

    def setup_browser(self):
        """Setup browser and return page object"""
        browser = self.p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context(viewport={'width': BROWSER_WIDTH, 'height': BROWSER_HEIGHT})
        page = context.new_page()
        page.goto(PAGE_URL)
        return browser, page
    
    def setup_browser_headless(self):
        """Setup headless browser for CI/CD"""
        browser = self.p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': BROWSER_WIDTH, 'height': BROWSER_HEIGHT})
        page = context.new_page()
        page.goto(PAGE_URL)
        return browser, page
    
    def setup_mobile_browser(self):
        """Setup mobile viewport for responsive testing"""
        browser = self.p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context(viewport={'width': 375, 'height': 667})  # Mobile size
        page = context.new_page()
        page.goto(PAGE_URL)
        return browser, page
```

### **Update `keywords/__init__.py`:**
```python
from .log_in import log_in_class
from .hamburger_menu import hamgurger_menu_class
from .products import products_class
from .setup import setup_class  # Add this line
```

---

## 🔐 **LOGIN CLASS TEMPLATE**

### **File: `keywords/log_in.py`**
```python
# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright
import os
import random

# ════════════════════════ VARIABLES ════════════════════════
INCORRECT_PASSWORD = "(FILL_WRONG_PASSWORD)"
INCORRECT_USER_NAME = "(FILL_WRONG_USERNAME)"
CORRECT_USER_NAME = ["(FILL_USER1)", "(FILL_USER2)", "(FILL_USER3)"]
CORRECT_PASSWORD = "(FILL_CORRECT_PASSWORD)"

# ════════════════════════ KEYWORDS ════════════════════════
class log_in_class():
    def __init__(self, page):
        self.page = page
    
    def incorrect_password(self):
        """Test login with wrong password"""
        # Test empty username
        self.page.fill("[id='password']", INCORRECT_PASSWORD) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Username is required" in self.page.content()
        self.page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "error_no_username.png"))
    
    def incorrect_username(self):
        """Test login with wrong username"""
        # Test empty password
        self.page.fill("[id='user-name']", INCORRECT_USER_NAME) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Password is required" in self.page.content()
        self.page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "error_no_password.png"))
    
    def incorrect_password_and_username(self):
        """Test login with wrong credentials"""
        self.page.fill("[id='user-name']", INCORRECT_USER_NAME) 
        self.page.fill("[id='password']", INCORRECT_PASSWORD) 
        self.page.click("[id='login-button']") 
        assert "Epic sadface: Username and password do not match" in self.page.content()
        self.page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "error_wrong_credentials.png"))
    
    def correct_password_and_username(self):
        """Test successful login"""
        self.page.fill("[id='user-name']", random.choice(CORRECT_USER_NAME)) 
        self.page.fill("[id='password']", CORRECT_PASSWORD) 
        self.page.click("[id='login-button']") 
        self.page.screenshot(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots", "successful_login.png"))
```

### **🔧 Customization Instructions:**
1. Replace `(FILL_WRONG_PASSWORD)` with actual wrong password
2. Replace `(FILL_WRONG_USERNAME)` with actual wrong username  
3. Replace `(FILL_USER1)`, etc. with valid usernames
4. Replace `(FILL_CORRECT_PASSWORD)` with actual password
5. Update selectors `[id='user-name']`, etc. to match your app
6. Modify assertion messages to match your app's error messages

---

## 🍔 **NAVIGATION MENU TEMPLATE**

### **File: `keywords/hamburger_menu.py`**
```python
# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
MENU_BUTTON_SELECTOR = "(FILL_MENU_BUTTON_SELECTOR)"
ABOUT_LINK_SELECTOR = "(FILL_ABOUT_LINK_SELECTOR)"
LOGOUT_LINK_SELECTOR = "(FILL_LOGOUT_LINK_SELECTOR)"
ALL_ITEMS_SELECTOR = "(FILL_ALL_ITEMS_SELECTOR)"

# ════════════════════════ KEYWORDS ════════════════════════
class hamburger_menu_class():
    def __init__(self, page):
        self.page = page
    
    def open_menu(self):
        """Open the hamburger menu"""
        self.page.locator(MENU_BUTTON_SELECTOR).click()
        # Add wait for menu to be visible if needed
        # self.page.wait_for_selector("(MENU_CONTAINER_SELECTOR)")
    
    def about(self):
        """Navigate to About page"""
        self.open_menu()
        self.page.locator(ABOUT_LINK_SELECTOR).click()
    
    def log_out(self):
        """Log out from the application"""
        self.open_menu()
        self.page.locator(LOGOUT_LINK_SELECTOR).click()
    
    def all_items(self):
        """Navigate to All Items page"""
        self.open_menu()
        self.page.locator(ALL_ITEMS_SELECTOR).click()
    
    def close_menu(self):
        """Close the hamburger menu if open"""
        # Add implementation if your app has a close button
        # self.page.locator("(CLOSE_BUTTON_SELECTOR)").click()
        pass
```

### **🔧 Customization Instructions:**
1. Replace `(FILL_MENU_BUTTON_SELECTOR)` with your menu button selector
2. Replace all `(FILL_*_SELECTOR)` variables with actual selectors
3. Add more menu items as needed
4. Implement `close_menu()` if your app supports it

---

## 🛒 **PRODUCTS CLASS TEMPLATE**

### **File: `keywords/products.py`**
```python
# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
# Product selectors - customize these for your application
PRODUCT_SELECTORS = {
    "product1": "[data-test=\"(FILL_PRODUCT1_SELECTOR)\"]",
    "product2": "[data-test=\"(FILL_PRODUCT2_SELECTOR)\"]", 
    "product3": "[data-test=\"(FILL_PRODUCT3_SELECTOR)\"]",
    "product4": "[data-test=\"(FILL_PRODUCT4_SELECTOR)\"]",
    "product5": "[data-test=\"(FILL_PRODUCT5_SELECTOR)\"]",
}

REMOVE_SELECTORS = {
    "product1": "[data-test=\"(FILL_REMOVE_PRODUCT1_SELECTOR)\"]",
    "product2": "[data-test=\"(FILL_REMOVE_PRODUCT2_SELECTOR)\"]",
    "product3": "[data-test=\"(FILL_REMOVE_PRODUCT3_SELECTOR)\"]",
    "product4": "[data-test=\"(FILL_REMOVE_PRODUCT4_SELECTOR)\"]",
    "product5": "[data-test=\"(FILL_REMOVE_PRODUCT5_SELECTOR)\"]",
}

# ════════════════════════ KEYWORDS ════════════════════════
class products_class():
    def __init__(self, page):
        self.page = page
    
    def add_to_cart_main_page(self):
        """Add multiple products to cart from main page"""
        for product_name, selector in PRODUCT_SELECTORS.items():
            self.page.locator(selector).click()
            print(f"✅ Added {product_name} to cart")
    
    def add_single_product(self, product_name):
        """Add a specific product to cart"""
        if product_name in PRODUCT_SELECTORS:
            self.page.locator(PRODUCT_SELECTORS[product_name]).click()
            print(f"✅ Added {product_name} to cart")
        else:
            print(f"❌ Product {product_name} not found")
    
    def remove_from_cart_main_page(self):
        """Remove all products from cart on main page"""
        for product_name, selector in REMOVE_SELECTORS.items():
            # Check if remove button exists before clicking
            if self.page.locator(selector).is_visible():
                self.page.locator(selector).click()
                print(f"✅ Removed {product_name} from cart")
    
    def remove_single_product(self, product_name):
        """Remove a specific product from cart"""
        if product_name in REMOVE_SELECTORS:
            if self.page.locator(REMOVE_SELECTORS[product_name]).is_visible():
                self.page.locator(REMOVE_SELECTORS[product_name]).click()
                print(f"✅ Removed {product_name} from cart")
        else:
            print(f"❌ Product {product_name} not found")
    
    def get_cart_count(self):
        """Get number of items in cart"""
        cart_badge = self.page.locator("(FILL_CART_BADGE_SELECTOR)")
        if cart_badge.is_visible():
            return cart_badge.text_content()
        return "0"
    
    def view_product_details(self, product_name):
        """Click on product to view details"""
        product_link_selector = f"(FILL_PRODUCT_LINK_BASE_SELECTOR){product_name}"
        self.page.locator(product_link_selector).click()
```

### **🔧 Customization Instructions:**
1. Replace all `(FILL_PRODUCT*_SELECTOR)` with actual product selectors
2. Replace `(FILL_REMOVE_PRODUCT*_SELECTOR)` with remove button selectors
3. Replace `(FILL_CART_BADGE_SELECTOR)` with cart count indicator
4. Add more products to the dictionaries as needed
5. Customize product names to match your application

---

## 🛠️ **KEYWORDS/__INIT__.PY TEMPLATE**

### **File: `keywords/__init__.py`**
```python
# Import all keyword classes for easy access
from .log_in import log_in_class
from .hamburger_menu import hamburger_menu_class  
from .products import products_class

# Add more imports as you create new keyword files:
# from .checkout import checkout_class
# from .user_profile import user_profile_class
# from .search import search_class
```

---

## 🎯 **ADDITIONAL CLASS TEMPLATES**

### **🛒 CHECKOUT CLASS TEMPLATE**
```python
# ════════════════════════ SETTINGS ════════════════════════
from playwright.sync_api import sync_playwright

# ════════════════════════ KEYWORDS ════════════════════════
class checkout_class():
    def __init__(self, page):
        self.page = page
    
    def go_to_cart(self):
        """Navigate to shopping cart"""
        self.page.locator("(FILL_CART_ICON_SELECTOR)").click()
    
    def proceed_to_checkout(self):
        """Start checkout process"""
        self.page.locator("(FILL_CHECKOUT_BUTTON_SELECTOR)").click()
    
    def fill_shipping_info(self, first_name, last_name, postal_code):
        """Fill shipping information"""
        self.page.locator("(FILL_FIRST_NAME_SELECTOR)").fill(first_name)
        self.page.locator("(FILL_LAST_NAME_SELECTOR)").fill(last_name)
        self.page.locator("(FILL_POSTAL_CODE_SELECTOR)").fill(postal_code)
        self.page.locator("(FILL_CONTINUE_BUTTON_SELECTOR)").click()
    
    def complete_order(self):
        """Complete the order"""
        self.page.locator("(FILL_FINISH_BUTTON_SELECTOR)").click()
        # Add assertion for success message
        # assert "Thank you" in self.page.content()
```

### **🔍 SEARCH CLASS TEMPLATE**
```python
class search_class():
    def __init__(self, page):
        self.page = page
    
    def search_product(self, search_term):
        """Search for a product"""
        self.page.locator("(FILL_SEARCH_BOX_SELECTOR)").fill(search_term)
        self.page.locator("(FILL_SEARCH_BUTTON_SELECTOR)").click()
    
    def filter_results(self, filter_option):
        """Apply filter to search results"""
        self.page.locator("(FILL_FILTER_DROPDOWN_SELECTOR)").select_option(filter_option)
```

---

## 💡 **BEST PRACTICES FOR KEYWORDS**

### **🎯 Structure Guidelines:**
1. **One functionality per class** (login, navigation, products, etc.)
2. **Use descriptive method names** that explain what they do
3. **Add docstrings** to explain each method
4. **Include error handling** and assertions
5. **Add screenshots** for important steps

### **🔧 Naming Conventions:**
- **Classes:** `functionality_class` (e.g., `log_in_class`)
- **Methods:** `action_description` (e.g., `add_to_cart_main_page`)
- **Variables:** `ALL_CAPS` for constants, `snake_case` for others

### **📝 Documentation:**
- Always add comments explaining complex logic
- Use section separators (════════) for organization
- Include customization instructions for each template