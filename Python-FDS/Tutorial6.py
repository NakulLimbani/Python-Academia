"""
*1) Apply unittest module in Python to perform arithmetic operations using functions on an IDE:*

You can use the `unittest` module to create test cases for your arithmetic operations functions. Here's an example of how to do it:

"""
import unittest
"""
# Define your arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

# Create a test class
class TestArithmeticOperations(unittest.TestCase):
    

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
    
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
    
    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)
    
    def test_divide(self):
        self.assertEqual(divide(8, 4), 2)
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
"""

"""You can run this script in your Python IDE to perform arithmetic operations using functions and ensure their correctness with unit tests.

*2) Set a breakpoint at a particular line using Python Standard Debugger (PDB):*

You can set a breakpoint in your code using the Python Standard Debugger (PDB). Here's how you can do it:
"""
import pdb

def addition():
    x = 5
    y = 10
    result = x + y
    
    # Set a breakpoint here
    pdb.set_trace()
    
    print("Result:", result)


addition()