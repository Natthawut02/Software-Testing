import unittest

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")  
        self.assertEqual(fizzbuzz(9), "Fizz")  

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")  
        self.assertEqual(fizzbuzz(10), "Buzz") 

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")  

    def test_number(self):
        self.assertEqual(fizzbuzz(2), "2")  
        self.assertEqual(fizzbuzz(7), "7") 

    def test_zero(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz") 

    def test_negative_numbers(self):
        self.assertEqual(fizzbuzz(-3), "Fizz")  
        self.assertEqual(fizzbuzz(-5), "Buzz")  
        self.assertEqual(fizzbuzz(-15), "FizzBuzz")  
        self.assertEqual(fizzbuzz(-7), "-7") 

if __name__ == "__main__":
    unittest.main()
