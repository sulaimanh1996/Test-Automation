# 🎯 PLAYWRIGHT ELEMENT SELECTORS & INTERACTION REFERENCE
Copy-paste templates for all element interactions

## 🔍 **LOCATOR REFERENCE GUIDE**

### **📌 COPY-PASTE TEMPLATES**

#### **ID SELECTOR**
```python
# Single element by ID
self.page.locator("#username").click()
self.page.locator("#password").fill("secret_sauce")
self.page.locator("#login-button").click()
```

#### **CLASS SELECTOR (Single Class)**
```python
# Single class
self.page.locator(".btn-primary").click()
self.page.locator(".inventory_item_name").click()
self.page.locator(".shopping_cart_link").click()
```

#### **CLASS SELECTOR (Multiple Classes)**
```python
# Multiple classes (no spaces between dots)
self.page.locator(".btn.btn-primary.btn-large").click()
self.page.locator(".inventory_item.inventory_item_available").hover()
```

#### **CLASS ATTRIBUTE (Exact Match)**
```python
# Exact class string match
self.page.locator("[class=\"btn btn_primary btn_small btn_inventory\"]").click()
self.page.locator("[class=\"inventory_item_name \"]").click()
```

#### **DATA-TEST ATTRIBUTE (Most Reliable)**
```python
# Data-test attribute (most reliable for testing)
self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
self.page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
self.page.locator("[data-test=\"shopping-cart-link\"]").click()
self.page.locator("[data-test=\"back-to-products\"]").click()
```

#### **NAME ATTRIBUTE**
```python
# Name attribute (forms)
self.page.locator("[name=\"user-name\"]").fill("standard_user")
self.page.locator("[name=\"password\"]").fill("secret_sauce")
self.page.locator("[name=\"submit\"]").click()
```

#### **TEXT CONTENT SELECTORS**
```python
# Click by visible text (exact match)
self.page.locator("text=Add to cart").click()
self.page.locator("text=Remove").click()
self.page.locator("text=Checkout").click()

# Click by partial text
self.page.locator("text=/Add to/").click()
self.page.locator("text=/Cart/").click()

# Has text filter (more flexible)
self.page.locator("button").filter(has_text="Add to cart").click()
self.page.locator("a").filter(has_text="Sauce Labs Backpack").click()
```

#### **LINK SELECTORS**
```python
# Links by href
self.page.locator("a[href='/inventory.html']").click()
self.page.locator("a[href*='item']").click()  # Contains 'item'

# Links by text
self.page.locator("a:has-text('About')").click()
self.page.locator("link=Logout").click()

# Links by title
self.page.locator("a[title='Go to product page']").click()
```

#### **BUTTON SELECTORS**
```python
# Button by type
self.page.locator("button[type='submit']").click()
self.page.locator("input[type='button']").click()

# Button by value
self.page.locator("input[value='Login']").click()

# Button containing text
self.page.locator("button:has-text('Add to cart')").click()
```

#### **INPUT FIELD SELECTORS**
```python
# Input by type
self.page.locator("input[type='text']").fill("username")
self.page.locator("input[type='password']").fill("password")
self.page.locator("input[type='email']").fill("user@example.com")

# Input by placeholder
self.page.locator("[placeholder=\"Username\"]").fill("standard_user")
self.page.locator("[placeholder=\"Password\"]").fill("secret_sauce")

# Textarea
self.page.locator("textarea[name='message']").fill("Hello World")
```

#### **DROPDOWN/SELECT SELECTORS**
```python
# Select dropdown
self.page.locator("select[name='country']").select_option("US")
self.page.locator("select").select_option(label="United States")
self.page.locator("select").select_option(index=1)

# Custom dropdown
self.page.locator(".dropdown-toggle").click()
self.page.locator(".dropdown-item:has-text('Option 1')").click()
```

#### **CHECKBOX & RADIO SELECTORS**
```python
# Checkbox
self.page.locator("input[type='checkbox']").check()
self.page.locator("input[type='checkbox']").uncheck()
self.page.locator("input[type='checkbox'][name='agree']").check()

# Radio button
self.page.locator("input[type='radio'][value='male']").check()
self.page.locator("input[type='radio'][name='gender']").first.check()
```

#### **IMAGE SELECTORS**
```python
# Image by alt text
self.page.locator("img[alt='Product image']").click()
self.page.locator("img[alt*='sauce']").click()

# Image by src
self.page.locator("img[src*='backpack']").click()
```

#### **ROLE SELECTOR (Accessibility)**
```python
# By role and name (best practice)
self.page.locator("role=button[name=\"Submit\"]").click()
self.page.locator("role=link[name=\"Home\"]").click()
self.page.locator("role=textbox[name=\"Username\"]").fill("user")
self.page.locator("role=combobox[name=\"Country\"]").select_option("US")
```

#### **XPATH SELECTOR**
```python
# XPath expressions (use sparingly)
self.page.locator("xpath=//button[@id='submit']").click()
self.page.locator("xpath=//a[contains(@href, 'product')]").click()
self.page.locator("xpath=//div[text()='Success']").wait_for()
```

#### **CSS SELECTOR (Advanced)**
```python
# Descendant selectors
self.page.locator(".inventory_container .inventory_item").first.click()
self.page.locator("form input[type='submit']").click()

# Sibling selectors
self.page.locator(".price + button").click()
self.page.locator("label ~ input").fill("value")

# Attribute contains
self.page.locator("[class*=\"btn-primary\"]").click()
self.page.locator("[id*=\"cart\"]").click()

# Pseudo selectors
self.page.locator("button:first-child").click()
self.page.locator("li:last-child").click()
self.page.locator("tr:nth-child(2)").click()
```

#### **NTH ELEMENT & FILTERING**
```python
# Select specific occurrence (0-based index)
self.page.locator(".inventory_item").nth(0).click()  # First item
self.page.locator(".inventory_item").nth(1).click()  # Second item
self.page.locator(".inventory_item").nth(-1).click() # Last item

# First and last
self.page.locator(".button").first.click()
self.page.locator(".button").last.click()

# Filter by text
self.page.locator(".inventory_item").filter(has_text="Backpack").click()

# Filter by locator
self.page.locator(".item").filter(self.page.locator(".price")).click()
```

## 🧭 **INTERACTION METHODS**

### **📱 CLICK ACTIONS**
```python
# Basic click
self.page.locator("button").click()

# Click with options
self.page.locator("button").click(button="right")        # Right click
self.page.locator("button").click(button="middle")       # Middle click
self.page.locator("button").click(modifiers=["Shift"])   # Shift+click
self.page.locator("button").click(modifiers=["Ctrl"])    # Ctrl+click
self.page.locator("button").click(force=True)            # Force click
self.page.locator("button").click(timeout=5000)          # With timeout

# Double click
self.page.locator("element").dblclick()

# Click at specific position
self.page.locator("canvas").click(position={"x": 100, "y": 200})
```

### **⌨️ INPUT ACTIONS**
```python
# Fill input field
self.page.locator("input").fill("Hello World")

# Clear and fill
self.page.locator("input").clear()
self.page.locator("input").fill("New Text")

# Type with delay (simulates human typing)
self.page.locator("input").type("Hello", delay=100)

# Press single keys
self.page.locator("input").press("Enter")
self.page.locator("input").press("Tab")
self.page.locator("input").press("Escape")
self.page.locator("input").press("ArrowDown")
self.page.locator("input").press("Home")
self.page.locator("input").press("End")

# Press key combinations
self.page.locator("input").press("Control+A")  # Select all
self.page.locator("input").press("Control+C")  # Copy
self.page.locator("input").press("Control+V")  # Paste
self.page.locator("input").press("Shift+Tab")  # Shift+Tab

# Press sequence
self.page.locator("input").press_sequentially("Hello World", delay=50)
```

### **☑️ FORM ACTIONS**
```python
# Checkbox
self.page.locator("input[type='checkbox']").check()      # Check
self.page.locator("input[type='checkbox']").uncheck()    # Uncheck
self.page.locator("input[type='checkbox']").set_checked(True)  # Set state

# Radio button
self.page.locator("input[type='radio'][value='yes']").check()

# Dropdown selection
self.page.locator("select").select_option("value1")           # By value
self.page.locator("select").select_option(label="Option 1")   # By visible text
self.page.locator("select").select_option(index=0)            # By index
self.page.locator("select").select_option(["val1", "val2"])   # Multiple values

# File upload
self.page.locator("input[type='file']").set_input_files("path/to/file.jpg")
self.page.locator("input[type='file']").set_input_files(["file1.jpg", "file2.png"])  # Multiple

# Clear file upload
self.page.locator("input[type='file']").set_input_files([])
```

### **🖱️ MOUSE ACTIONS**
```python
# Hover
self.page.locator("element").hover()

# Hover with offset
self.page.locator("element").hover(position={"x": 10, "y": 10})

# Drag and drop
self.page.locator(".source").drag_to(self.page.locator(".target"))

# Drag and drop with offset
self.page.locator(".draggable").drag_to(
    self.page.locator(".target"), 
    target_position={"x": 50, "y": 50}
)

# Mouse wheel
self.page.locator("element").wheel(delta_x=0, delta_y=100)  # Scroll down
```

### **📄 SCROLLING ACTIONS**
```python
# Scroll element into view
self.page.locator("element").scroll_into_view_if_needed()

# Scroll to element
self.page.locator("element").scroll_to()

# Page scrolling
self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")  # Bottom
self.page.evaluate("window.scrollTo(0, 0)")  # Top
```

## ⏱️ **WAITING & VALIDATION**

### **⏳ WAIT METHODS**
```python
# Wait for element to appear
self.page.locator("element").wait_for()

# Wait for specific states
self.page.locator("element").wait_for(state="visible")    # Default
self.page.locator("element").wait_for(state="hidden")     # Wait to disappear
self.page.locator("element").wait_for(state="attached")   # Attached to DOM
self.page.locator("element").wait_for(state="detached")   # Removed from DOM

# Wait with timeout
self.page.locator("element").wait_for(timeout=5000)  # 5 seconds
self.page.locator("element").wait_for(timeout=30000) # 30 seconds

# Wait for count
self.page.locator(".item").wait_for(state="attached")
```

### **✅ VALIDATION METHODS**
```python
# Visibility checks
if self.page.locator("element").is_visible():
    print("✅ Element is visible")

if self.page.locator("element").is_hidden():
    print("✅ Element is hidden")

# State checks
if self.page.locator("input").is_enabled():
    print("✅ Input is enabled")

if self.page.locator("input").is_disabled():
    print("✅ Input is disabled")

if self.page.locator("checkbox").is_checked():
    print("✅ Checkbox is checked")

# Get element properties
text = self.page.locator("element").text_content()
inner_text = self.page.locator("element").inner_text()
inner_html = self.page.locator("element").inner_html()

# Get attribute values
value = self.page.locator("input").input_value()
class_attr = self.page.locator("element").get_attribute("class")
href = self.page.locator("a").get_attribute("href")

# Count elements
count = self.page.locator(".item").count()
print(f"Found {count} items")

# Get all text contents
texts = self.page.locator(".item").all_text_contents()
```

### **🔍 ELEMENT INFORMATION**
```python
# Get element box (position and size)
box = self.page.locator("element").bounding_box()
# Returns: {'x': 100, 'y': 200, 'width': 150, 'height': 50}

# Take screenshot of element
self.page.locator("element").screenshot(path="element.png")

# Evaluate JavaScript on element
result = self.page.locator("element").evaluate("el => el.clientHeight")
```

## 🎯 **REAL-WORLD EXAMPLES FROM PROJECT_02**

### **🔐 Login Page Examples**
```python
# SauceDemo login flow
def login_flow(self):
    # Fill username
    self.page.locator("#user-name").fill("standard_user")
    
    # Fill password  
    self.page.locator("#password").fill("secret_sauce")
    
    # Click login button
    self.page.locator("#login-button").click()
    
    # Verify successful login
    self.page.locator(".title").wait_for()
    assert self.page.locator(".title").text_content() == "PRODUCTS"
```

### **🛒 Product Page Examples**
```python
# Product interactions
def product_interactions(self):
    # Add specific product to cart
    self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    
    # Click on product name to view details
    self.page.locator(".inventory_item_name").filter(has_text="Sauce Labs Backpack").click()
    
    # Go back to products
    self.page.locator("[data-test=\"back-to-products\"]").click()
    
    # Remove from cart
    self.page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
    
    # Sort products
    self.page.locator(".product_sort_container").select_option("lohi")  # Price low to high
```

### **🛒 Shopping Cart Examples**
```python
# Cart operations
def cart_operations(self):
    # Go to cart
    self.page.locator(".shopping_cart_link").click()
    
    # Verify item in cart
    cart_items = self.page.locator(".cart_item").count()
    assert cart_items > 0
    
    # Remove item from cart
    self.page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
    
    # Continue shopping
    self.page.locator("[data-test=\"continue-shopping\"]").click()
    
    # Checkout
    self.page.locator("[data-test=\"checkout\"]").click()
```

### **🍔 Navigation Menu Examples**
```python
# Hamburger menu interactions
def menu_navigation(self):
    # Open menu
    self.page.locator("#react-burger-menu-btn").click()
    
    # Wait for menu to appear
    self.page.locator(".bm-menu").wait_for(state="visible")
    
    # Click menu items
    self.page.locator("#inventory_sidebar_link").click()  # All Items
    self.page.locator("#about_sidebar_link").click()      # About
    self.page.locator("#logout_sidebar_link").click()     # Logout
    
    # Close menu
    self.page.locator("#react-burger-cross-btn").click()
```

### **📋 Form Examples (Checkout)**
```python
# Checkout form
def checkout_form(self):
    # Fill checkout information
    self.page.locator("[data-test=\"firstName\"]").fill("John")
    self.page.locator("[data-test=\"lastName\"]").fill("Doe")
    self.page.locator("[data-test=\"postalCode\"]").fill("12345")
    
    # Continue
    self.page.locator("[data-test=\"continue\"]").click()
    
    # Finish order
    self.page.locator("[data-test=\"finish\"]").click()
    
    # Verify success
    success_message = self.page.locator(".complete-header").text_content()
    assert "THANK YOU" in success_message
```

## 🎨 **ADVANCED SELECTORS**

### **🔗 COMBINING SELECTORS**
```python
# Multiple conditions
self.page.locator("button.btn-primary[data-test='submit']").click()

# Parent-child relationships
self.page.locator(".inventory_item:has(.inventory_item_name:text('Backpack'))").click()

# Locator chaining
self.page.locator(".inventory_container").locator(".inventory_item").first.click()

# Filter chains
self.page.locator(".item").filter(has_text="Sauce").filter(self.page.locator(".price")).click()
```

### **🎯 PRECISE TARGETING**
```python
# Get element containing specific child
self.page.locator(".item:has(button:text('Add to cart'))").click()

# Get element by position in list
self.page.locator(".item >> nth=1").click()  # Second item

# Get by exact text match
self.page.locator("text='Add to cart'").click()  # Exact match
self.page.locator("text=/Add to cart/i").click()  # Case insensitive regex
```

## 💡 **BEST PRACTICES**

### **🎯 Selector Priority (Most Reliable → Least Reliable)**
1. **`data-test` attributes** - Most stable for testing
2. **`id` attributes** - Usually unique and stable  
3. **`role` selectors** - Accessibility-friendly
4. **`name` attributes** - Good for forms
5. **Specific class combinations** - Better than single classes
6. **Text content** - Can change with translations
7. **Generic selectors** - Avoid if possible
8. **XPath** - Most fragile, use as last resort

### **🔧 Selector Tips**
```python
# ✅ GOOD - Specific and stable
self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

# ✅ GOOD - Accessibility-friendly
self.page.locator("role=button[name='Add to cart']").click()

# ⚠️ OKAY - Can work but less stable
self.page.locator(".btn-primary").click()

# ❌ BAD - Too generic, unreliable
self.page.locator("button").click()
self.page.locator("div").click()
```

### **🔄 Error Handling**
```python
# Check if element exists before interacting
if self.page.locator("element").count() > 0:
    self.page.locator("element").click()

# Try-catch for optional elements
try:
    self.page.locator("optional-element").click(timeout=2000)
except:
    print("Optional element not found, continuing...")

# Wait with error handling
try:
    self.page.locator("element").wait_for(timeout=5000)
    self.page.locator("element").click()
except TimeoutError:
    print("Element not found within timeout")
```

## 🆘 **TROUBLESHOOTING GUIDE**

### **Common Issues & Solutions:**

#### **🔍 Element Not Found**
```python
# Problem: Element not found
# ❌ self.page.locator("#nonexistent").click()

# Solutions:
# ✅ Wait for element
self.page.locator("#element").wait_for()
self.page.locator("#element").click()

# ✅ Check if exists
if self.page.locator("#element").count() > 0:
    self.page.locator("#element").click()

# ✅ Use try-catch
try:
    self.page.locator("#element").click(timeout=5000)
except TimeoutError:
    print("Element not found")
```

#### **🎯 Multiple Elements Found**
```python
# Problem: Multiple elements, clicks first one
# ❌ self.page.locator(".button").click()  

# Solutions:
# ✅ Select specific element
self.page.locator(".button").nth(1).click()  # Second button
self.page.locator(".button").first.click()   # First button
self.page.locator(".button").last.click()    # Last button

# ✅ Filter by text
self.page.locator(".button").filter(has_text="Save").click()

# ✅ Use more specific selector
self.page.locator(".button[data-test='save-button']").click()
```

#### **👻 Element Not Clickable**
```python
# Problem: Element exists but not clickable
# ❌ self.page.locator("#hidden").click()

# Solutions:
# ✅ Wait for visibility
self.page.locator("#element").wait_for(state="visible")
self.page.locator("#element").click()

# ✅ Force click (if element is covered)
self.page.locator("#element").click(force=True)

# ✅ Scroll into view first
self.page.locator("#element").scroll_into_view_if_needed()
self.page.locator("#element").click()
```

#### **⏱️ Timing Issues**
```python
# Problem: Element appears/disappears too quickly
# ❌ self.page.locator("#dynamic").click()

# Solutions:
# ✅ Explicit waits
self.page.locator("#element").wait_for(state="visible")
self.page.locator("#element").click()

# ✅ Wait for stable state
self.page.wait_for_load_state("networkidle")
self.page.locator("#element").click()

# ✅ Custom wait conditions
self.page.wait_for_function("document.querySelector('#element').offsetHeight > 0")
```

### **🔧 Debug Tips**
```python
# Screenshot for debugging
self.page.screenshot(path="debug.png")

# Print element info
element = self.page.locator("#element")
print(f"Count: {element.count()}")
print(f"Visible: {element.is_visible()}")
print(f"Text: {element.text_content()}")

# Highlight element (for visual debugging)
self.page.locator("#element").highlight()

# Get all matching elements
elements = self.page.locator(".item").element_handles()
print(f"Found {len(elements)} elements")
```

## 📚 **QUICK REFERENCE CHEAT SHEET**

### **Most Common Selectors**
```python
# By ID
"#elementId"

# By Class  
".className"

# By Data Test (recommended)
"[data-test='value']"

# By Text
"text=Button Text"

# By Role (accessibility)
"role=button[name='Submit']"

# Multiple Conditions
"button.primary[data-test='save']"
```

### **Most Common Actions**
```python
.click()                    # Click element
.fill("text")              # Fill input
.select_option("value")    # Select dropdown
.check()                   # Check checkbox
.hover()                   # Hover mouse
.wait_for()               # Wait for element
.is_visible()             # Check visibility
.text_content()           # Get text
```

This reference guide should give you comprehensive coverage of Playwright selectors and interactions for your automation testing! 🚀