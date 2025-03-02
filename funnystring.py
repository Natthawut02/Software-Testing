def funnyString(s):
    reversed_s = s[::-1]
    diff_s = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)]
    diff_reversed = [abs(ord(reversed_s[i]) - ord(reversed_s[i+1])) for i in range(len(reversed_s)-1)]
    
    if diff_s == diff_reversed:
        return "Funny"
    else:
        return "Not Funny"
    
if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')
        
    fptr.close()



 # Test Case
import unittest

class TestFunnyString(unittest.TestCase):
    def test_funny_string(self):
        # Test Case 1: สตริง "Funny"
        self.assertEqual(funnyString("acxz"), "Funny")
        
        # Test Case 2: สตริง "Not Funny"
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        
        # Test Case 3: สตริงที่มีตัวอักษรซ้ำกัน
        self.assertEqual(funnyString("aaaa"), "Funny")
        
        # Test Case 4: สตริงที่มีความยาว 2 ตัวอักษร
        self.assertEqual(funnyString("ab"), "Funny")
        
        # Test Case 5: สตริงที่มีตัวอักษรผสม
        self.assertEqual(funnyString("abba"), "Funny")
        
        # Test Case 6: สตริงที่มีตัวอักษรผสมและไม่ "Funny"
        self.assertEqual(funnyString("abcd"), "Funny")
        
        # Test Case 7: สตริงที่มีตัวอักษรพิเศษ
        self.assertEqual(funnyString("!@#$"), "Not Funny")

if __name__ == '__main__':
    unittest.main()