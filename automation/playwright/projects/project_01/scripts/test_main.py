# tests/test_main.py
import scripts.keywords as keywords

def test_full_flow():
    keywords.LOG_IN()
    keywords.PRODUCT_PAGE()