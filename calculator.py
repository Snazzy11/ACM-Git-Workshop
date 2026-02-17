"""
Simple Calculator Program
CS Club Git Workshop Project
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Bug: Could divide by zero
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

def main():
    print("Welcome to Calculator!")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulo")
    
    choice = int(input("Enter operation (1-6): "))
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    elif choice == 5:
        result = power(num1, num2)
    elif choice == 6:
        result = modulo(num1, num2)
    else:
        print("Invalid choice!")
        return
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
