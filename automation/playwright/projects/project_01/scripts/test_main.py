# tests/test_main.py
import scripts.keywords as keywords

def test_full_flow():
    keywords.log_in()
    keywords.products()
