# 🧪 TEST FILE TEMPLATES
Copy-paste test structures based on PROJECT_02 with improved patterns

## 🎯 **MAIN TEST TEMPLATE (IMPROVED)**

### **File: `test_cases/test_main.py`**
```python
# ════════════════════════ SETTINGS ════════════════════════
from keywords import log_in_class
from keywords import hamgurger_menu_class
from keywords import products_class
from keywords import setup_class
from playwright.sync_api import sync_playwright

# ════════════════════════ VARIABLES ════════════════════════
PAGE_URL = "https://www.saucedemo.com"  # Replace with your app URL
BROWSER_WIDTH = 1920
BROWSER_HEIGHT = 1080

# ════════════════════════ TESTCASE ════════════════════════
def test_user_experience():
    """Complete user journey test - improved class-based setup"""
    with sync_playwright() as p:
        # Class-based browser setup (consistent with other handlers)
        setup_handler = setup_class(p)
        browser, page = setup_handler.setup_browser()

        # Initialize all keyword classes
        login_handler = log_in_class(page)
        hamburger_handler = hamgurger_menu_class(page)
        product_handler = products_class(page)

        try:
            # Test login scenarios
            login_handler.incorrect_password()
            login_handler.incorrect_username()
            login_handler.incorrect_password_and_username()
            login_handler.correct_password_and_username()

            # Test navigation
            hamburger_handler.about()
            page.go_back()
            hamburger_handler.log_out()
            
            # Login again for product testing
            login_handler.correct_password_and_username()
            hamburger_handler.all_items()

            # Test product functionality
            product_handler.add_to_cart_main_page()
            product_handler.remove_from_cart_main_page()
            product_handler.view_products()
            
        finally:
            # Always cleanup browser
            browser.close()

def test_login_only():
    """Focused test - login scenarios only"""
    with sync_playwright() as p:
        setup_handler = setup_class(p)
        browser, page = setup_handler.setup_browser()
        
        login_handler = log_in_class(page)
        
        try:
            login_handler.correct_password_and_username()
            # Add assertions here
            assert "inventory" in page.url
            
        finally:
            browser.close()

def test_products_only():
    """Focused test - product functionality only"""
    with sync_playwright() as p:
        setup_handler = setup_class(p)
        browser, page = setup_handler.setup_browser()
        
        login_handler = log_in_class(page)
        product_handler = products_class(page)
        
        try:
            # Quick login
            login_handler.correct_password_and_username()
            
            # Test products
            product_handler.add_to_cart_main_page()
            product_handler.view_products()
            
        finally:
            browser.close()
```

---

## 🔧 **SETUP PATTERNS**

### **🎯 Basic Setup (Standard)**
```python
def test_example():
    with sync_playwright() as p:
        setup_handler = setup_class(p)
        browser, page = setup_handler.setup_browser()
        
        # Your test code here
        
        browser.close()
```

### **🎯 Headless Setup (CI/CD)**
```python
def test_headless():
    with sync_playwright() as p:
        setup_handler = setup_class(p)
        browser, page = setup_handler.setup_browser_headless()
        
        # Your test code here
        
        browser.close()
```

### **🎯 Mobile Setup (Responsive Testing)**
```python
def test_mobile():
    with sync_playwright() as p:
        setup_handler = setup_class(p)
        browser, page = setup_handler.setup_mobile_browser()
        
        # Your test code here
        
        browser.close()
```

### **🎯 Multiple Handlers Pattern**
```python
def test_full_workflow():
    with sync_playwright() as p:
        # Setup
        setup_handler = setup_class(p)
        browser, page = setup_handler.setup_browser()
        
        # Initialize all handlers
        login_handler = log_in_class(page)
        nav_handler = hamgurger_menu_class(page)
        product_handler = products_class(page)
        
        try:
            # Use handlers
            login_handler.correct_password_and_username()
            nav_handler.all_items()
            product_handler.add_to_cart_main_page()
            
        finally:
            browser.close()
```

def test_login_only():
    """Focused test for login functionality only"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()
        page.goto(PAGE_LINK_LOGIN)

        login_handler = log_in_class(page)
        
        # Test different login scenarios
        login_handler.incorrect_password()
        login_handler.correct_password_and_username()
        
        browser.close()

def test_products_only():
    """Focused test for product functionality"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()
        page.goto(PAGE_LINK_LOGIN)

        login_handler = log_in_class(page)
        product_handler = products_class(page)
        
        # Login first
        login_handler.correct_password_and_username()
        
        # Test product actions
        product_handler.add_to_cart_main_page()
        product_handler.remove_from_cart_main_page()
        
        browser.close()
```

### **🔧 Customization Instructions:**
1. Replace `(FILL_YOUR_APP_URL_HERE)` with your application URL
2. Add/remove keyword class imports based on your needs
3. Modify test scenarios to match your application flow
4. Adjust browser settings (`headless`, `slow_mo`) as needed

---

## 🎯 **SPECIALIZED TEST TEMPLATES**

### **🔐 LOGIN-FOCUSED TEST TEMPLATE**
```python
# ════════════════════════ SETTINGS ════════════════════════
from keywords import log_in_class
from playwright.sync_api import sync_playwright
import pytest

# ════════════════════════ VARIABLES ════════════════════════
PAGE_LINK_LOGIN = "(FILL_YOUR_LOGIN_URL)"

# ════════════════════════ TEST CLASS ════════════════════════
class TestLoginFunctionality:
    """Test class for all login-related scenarios"""
    
    def setup_method(self):
        """Setup method run before each test"""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False, slow_mo=100)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto(PAGE_LINK_LOGIN)
        self.login_handler = log_in_class(self.page)
    
    def teardown_method(self):
        """Cleanup method run after each test"""
        self.browser.close()
        self.playwright.stop()
    
    def test_invalid_password(self):
        """Test login with invalid password"""
        self.login_handler.incorrect_password()
    
    def test_invalid_username(self):
        """Test login with invalid username"""
        self.login_handler.incorrect_username()
    
    def test_invalid_credentials(self):
        """Test login with both invalid username and password"""
        self.login_handler.incorrect_password_and_username()
    
    def test_valid_login(self):
        """Test successful login"""
        self.login_handler.correct_password_and_username()
        # Add assertions for successful login
        assert "inventory" in self.page.url.lower()
```

### **🛒 PRODUCTS-FOCUSED TEST TEMPLATE**
```python
# ════════════════════════ SETTINGS ════════════════════════
from keywords import log_in_class, products_class
from playwright.sync_api import sync_playwright
import pytest

# ════════════════════════ VARIABLES ════════════════════════
PAGE_LINK_LOGIN = "(FILL_YOUR_LOGIN_URL)"

# ════════════════════════ TEST CLASS ════════════════════════
class TestProductFunctionality:
    """Test class for product-related scenarios"""
    
    def setup_method(self):
        """Setup method run before each test - includes login"""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False, slow_mo=100)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto(PAGE_LINK_LOGIN)
        
        # Login before each product test
        self.login_handler = log_in_class(self.page)
        self.login_handler.correct_password_and_username()
        
        # Initialize product handler
        self.product_handler = products_class(self.page)
    
    def teardown_method(self):
        """Cleanup method run after each test"""
        self.browser.close()
        self.playwright.stop()
    
    def test_add_all_products(self):
        """Test adding all products to cart"""
        initial_count = self.product_handler.get_cart_count()
        self.product_handler.add_to_cart_main_page()
        final_count = self.product_handler.get_cart_count()
        # Add assertion to verify cart count increased
        
    def test_add_and_remove_products(self):
        """Test adding and then removing products"""
        self.product_handler.add_to_cart_main_page()
        self.product_handler.remove_from_cart_main_page()
        # Verify cart is empty
        
    def test_single_product_workflow(self):
        """Test adding and removing a single product"""
        self.product_handler.add_single_product("product1")
        cart_count = self.product_handler.get_cart_count()
        assert cart_count == "1"
        
        self.product_handler.remove_single_product("product1")
        cart_count = self.product_handler.get_cart_count()
        assert cart_count == "0"
```

---

## 🧪 **ADVANCED TEST PATTERNS**

### **🔄 PARAMETRIZED TESTS**
```python
import pytest
from keywords import log_in_class
from playwright.sync_api import sync_playwright

# Test data
LOGIN_TEST_DATA = [
    ("", "valid_password", "Username is required"),
    ("valid_user", "", "Password is required"),
    ("invalid_user", "invalid_pass", "Username and password do not match"),
]

@pytest.mark.parametrize("username,password,expected_error", LOGIN_TEST_DATA)
def test_login_scenarios(username, password, expected_error):
    """Parametrized test for multiple login scenarios"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("(FILL_YOUR_URL)")
        
        # Fill credentials
        page.fill("[id='user-name']", username)
        page.fill("[id='password']", password)
        page.click("[id='login-button']")
        
        # Verify error message
        assert expected_error in page.content()
        
        browser.close()
```

### **🏷️ TEST MARKERS & TAGS**
```python
import pytest
from keywords import log_in_class, products_class
from playwright.sync_api import sync_playwright

@pytest.mark.smoke
def test_basic_login():
    """Smoke test for basic login functionality"""
    # Basic login test
    pass

@pytest.mark.regression  
def test_complete_user_journey():
    """Full regression test"""
    # Complete user flow
    pass

@pytest.mark.critical
def test_checkout_process():
    """Critical business functionality"""
    # Checkout flow
    pass

# Run specific tests:
# pytest -m smoke
# pytest -m "smoke or critical"
# pytest -m "not regression"
```

---

## 📁 **TEST STRUCTURE VARIATIONS**

### **📂 Multiple Test Files Structure**
```
test_cases/
├── __init__.py
├── test_main.py           # Main user journey
├── test_login.py          # Login-specific tests
├── test_products.py       # Product-specific tests
├── test_navigation.py     # Navigation tests
└── test_checkout.py       # Checkout flow tests
```

### **📄 Individual Test File Template**
```python
# test_login.py
from keywords import log_in_class
from playwright.sync_api import sync_playwright
import pytest

def test_successful_login():
    """Test valid login credentials"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("(FILL_YOUR_URL)")
        
        login_handler = log_in_class(page)
        login_handler.correct_password_and_username()
        
        # Verify successful login
        assert "dashboard" in page.url.lower() or "inventory" in page.url.lower()
        
        browser.close()

def test_failed_login():
    """Test invalid login credentials"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto("(FILL_YOUR_URL)")
        
        login_handler = log_in_class(page)
        login_handler.incorrect_password_and_username()
        
        browser.close()
```

---

## ⚙️ **CONFIGURATION TIPS**

### **🎯 Test Discovery Rules**
- Files must start with `test_` or end with `_test.py`
- Functions must start with `test_`
- Classes must start with `Test` (capital T)

### **🔧 Common pytest.ini for Tests**
```ini
[pytest]
# Basic configuration
addopts = --alluredir=allure-results --clean-alluredir -v
testpaths = test_cases

# Advanced configuration with markers
markers =
    smoke: Quick smoke tests
    regression: Full regression suite
    critical: Critical business functionality
    slow: Tests that take a long time
```

### **💡 Best Practices**
1. **Keep tests independent** - each test should be able to run alone
2. **Use descriptive test names** - explain what the test validates
3. **Add docstrings** to explain test purpose
4. **Clean up resources** - always close browsers
5. **Use assertions** to verify expected results
6. **Group related tests** in classes or separate files
7. **Use setup/teardown** methods to avoid code duplication

---

## 🚀 **QUICK START CHECKLIST**

- [ ] Copy test template to your `test_cases/` directory
- [ ] Replace `(FILL_YOUR_APP_URL_HERE)` with actual URL
- [ ] Update keyword class imports based on your needs
- [ ] Customize test scenarios for your application
- [ ] Run test: `pytest test_cases/test_main.py`
- [ ] Verify HTML report is generated
- [ ] Add more specific tests as needed