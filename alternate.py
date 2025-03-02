def alternate(s):
    unique_chars = list(set(s))
    max_length = 0
    
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            temp = [c for c in s if c == char1 or c == char2]
            valid = True
            for k in range(1, len(temp)):
                if temp[k] == temp[k - 1]:
                    valid = False
                    break
            if valid:
                max_length = max(max_length, len(temp))
    
    return max_length




# Test Cases
import unittest

class TestAlternate(unittest.TestCase):
    def test_alternate(self):
        self.assertEqual(alternate("abaacdabd"), 4)
        self.assertEqual(alternate("beabeefeab"), 5)
        self.assertEqual(alternate("aaaa"), 0)
        self.assertEqual(alternate("abababab"), 8)
        self.assertEqual(alternate("abcabcabc"), 6)
        self.assertEqual(alternate("a"), 0)
        self.assertEqual(alternate("ab"), 2)
        self.assertEqual(alternate("abc"), 2)
        self.assertEqual(alternate("abacaba"), 5)
        self.assertEqual(alternate("abacabad"), 5)
