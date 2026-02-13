"""
Test Suite for Workshop Code
Run this to check if your fixes work!
"""

from calculator import add, subtract, multiply, divide, power, modulo
from utils import is_palindrome, factorial, fibonacci, reverse_string, count_vowels, is_prime

def test_calculator():
    """Test calculator functions"""
    print("Testing Calculator...")
    
    # Basic operations
    assert add(5, 3) == 8, "Addition failed"
    assert subtract(10, 4) == 6, "Subtraction failed"
    assert multiply(6, 7) == 42, "Multiplication failed"
    
    # Division
    try:
        result = divide(10, 2)
        assert result == 5, "Division failed"
        print("✓ Division works")
    except:
        print("✗ Division still has bugs")
    
    # Division by zero
    try:
        divide(10, 0)
        print("✗ Division by zero should be handled")
    except ZeroDivisionError:
        print("✗ Division by zero crashes (needs fix)")
    except:
        print("✓ Division by zero is handled")
    
    # Power
    assert power(2, 3) == 8, "Power failed"
    
    # Modulo
    try:
        result = modulo(10, 3)
        assert result == 1, "Modulo failed"
        print("✓ Modulo works")
    except:
        print("✗ Modulo still has bugs")
    
    print()

def test_utils():
    """Test utility functions"""
    print("Testing Utilities...")
    
    # Palindrome
    assert is_palindrome("racecar") == True, "Palindrome check failed"
    assert is_palindrome("hello") == False, "Palindrome check failed"
    print("✓ Palindrome works")
    
    # Factorial
    try:
        result = factorial(5)
        assert result == 120, f"Factorial failed: expected 120, got {result}"
        print("✓ Factorial works")
    except AssertionError:
        print("✗ Factorial returns wrong value")
    except:
        print("✗ Factorial still has bugs")
    
    # Fibonacci
    try:
        result = fibonacci(7)
        expected = [0, 1, 1, 2, 3, 5, 8]
        assert result == expected, f"Fibonacci failed: expected {expected}, got {result}"
        print("✓ Fibonacci works")
    except AssertionError as e:
        print(f"✗ Fibonacci returns wrong sequence: {e}")
    
    # Reverse string
    assert reverse_string("hello") == "olleh", "Reverse string failed"
    print("✓ Reverse string works")
    
    # Count vowels
    assert count_vowels("hello") == 2, "Count vowels failed"
    print("✓ Count vowels works")
    
    # Prime check
    assert is_prime(7) == True, "Prime check failed"
    assert is_prime(4) == False, "Prime check failed"
    print("✓ Prime check works (but may be slow)")
    
    print()

def run_all_tests():
    """Run all test suites"""
    print("=" * 50)
    print("Running Workshop Tests")
    print("=" * 50)
    print()
    
    try:
        test_calculator()
    except Exception as e:
        print(f"Calculator tests crashed: {e}")
        print()
    
    try:
        test_utils()
    except Exception as e:
        print(f"Utility tests crashed: {e}")
        print()
    
    print("=" * 50)
    print("Testing Complete!")
    print("=" * 50)
    print()
    print("Fix any ✗ items above to complete your challenges!")

if __name__ == "__main__":
    run_all_tests()
