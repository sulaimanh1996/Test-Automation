# 🗂️ PROJECT STRUCTURE & FILE ORGANIZATION
Based on PROJECT_02 architecture with improved setup patterns

## 📁 **COMPLETE PROJECT STRUCTURE**
```
project_name/
├── __init__.py                     # Root package file
├── pytest.ini                     # Pytest configuration
├── allure-results/                 # Auto-generated test results
│   └── [JSON files]               # Allure test data
├── keywords/                       # Reusable automation classes
│   ├── __init__.py                # Package imports
│   ├── setup.py                   # Browser setup class ⭐ NEW
│   ├── log_in.py                  # Login functionality
│   ├── hamburger_menu.py          # Navigation menu actions
│   └── products.py                # Product page interactions
└── test_cases/                     # Test execution files
    ├── __init__.py                # Package file
    └── test_main.py               # Main test scenarios
```

## 📋 **FILE PURPOSES & CONTENT**

### **🔧 Root Files**

#### **`__init__.py` (Root)**
```python
# Project root package
```

#### **`pytest.ini`**
```ini
[pytest]
addopts = --alluredir=allure-results --clean-alluredir
testpaths = test_cases
```

### **📁 keywords/ Directory**
*Contains reusable automation classes organized by functionality*

#### **`keywords/__init__.py` (UPDATED)**
```python
from .log_in import log_in_class
from .hamburger_menu import hamgurger_menu_class
from .products import products_class
from .setup import setup_class  # ⭐ NEW - Browser setup class
```

#### **File Naming Convention:**
- `setup.py` - Browser initialization & configuration ⭐ **NEW**
- `log_in.py` - Authentication & login flows
- `hamburger_menu.py` - Navigation menu interactions
- `products.py` - Product-related actions
- Add more as needed: `checkout.py`, `user_profile.py`, etc.

### **📁 test_cases/ Directory**
*Contains actual test scenarios and execution logic*

#### **`test_cases/__init__.py`**
```python
# Test cases package
```

#### **File Naming Convention:**
- Files MUST start with `test_` for pytest discovery
- `test_main.py` - Main user journey tests
- `test_login.py` - Login-specific tests
- `test_checkout.py` - Checkout flow tests

## 🎯 **WHY THIS STRUCTURE?**

### **Separation of Concerns:**
- **`keywords/`** = What CAN be done (reusable actions)
- **`test_cases/`** = What SHOULD be tested (business scenarios)

### **Benefits:**
1. **Reusability** - Keywords used across multiple tests
2. **Maintainability** - Changes in one place affect all tests
3. **Readability** - Tests focus on business logic, not implementation
4. **Scalability** - Easy to add new functionality

## 📝 **COPY-PASTE STRUCTURE CREATION**

### **Quick Setup Commands:**
```powershell
# Create all directories
mkdir keywords, test_cases

# Create all __init__.py files
ni __init__.py
ni keywords\__init__.py  
ni test_cases\__init__.py

# Create main files
ni pytest.ini
ni keywords\log_in.py
ni keywords\hamburger_menu.py
ni keywords\products.py
ni test_cases\test_main.py
```

### **Verification Commands:**
```powershell
# Check structure
tree /f

# Should show:
# │   __init__.py
# │   pytest.ini
# ├───keywords
# │       hamburger_menu.py
# │       log_in.py
# │       products.py
# │       __init__.py
# └───test_cases
#         test_main.py
#         __init__.py
```

## 🔄 **IMPORT FLOW**

### **How Imports Work:**
1. **Test file imports from keywords:**
   ```python
   from keywords import log_in_class, products_class
   ```

2. **Keywords __init__.py handles the imports:**
   ```python
   from .log_in import log_in_class
   ```

3. **Individual keyword files contain classes:**
   ```python
   class log_in_class():
       def __init__(self, page):
           self.page = page
   ```

## ⚠️ **IMPORTANT NOTES**

### **__init__.py Requirements:**
- **EVERY directory needs `__init__.py`** to be a Python package
- **Root `__init__.py`** - Makes project importable
- **keywords `__init__.py`** - Exports all classes for easy import
- **test_cases `__init__.py`** - Enables pytest discovery

### **Naming Conventions:**
- **Directories:** lowercase with underscores
- **Files:** lowercase with underscores  
- **Classes:** lowercase with underscores + `_class`
- **Test files:** MUST start with `test_`

### **File Organization Tips:**
- **One main functionality per keyword file**
- **Group related actions in the same class**
- **Keep test files focused on specific user journeys**
- **Use descriptive file names that match functionality**