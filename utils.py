"""
Utility Functions
CS Club Git Workshop Project
"""

def is_palindrome(text):
    """Check if a string is a palindrome"""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def factorial(n):
    """Calculate factorial of n"""
    if n == 0:
        return 1
    # BUG: Missing return statement
    n * factorial(n - 1)

def fibonacci(n):
    """Generate fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    # BUG: Off-by-one error
    for i in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiou"
    count = 0
    
    for char in text.lower():
        if char in vowels:
            count += 1
    
    return count

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    
    # BUG: Inefficient algorithm, should only check up to sqrt(n)
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
