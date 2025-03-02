import unittest
def caesar_cipher(s, k):
    result = ""
    k %= 26
    for char in s:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char
    return result


class TestCaesarCipher(unittest.TestCase):
    def test_shift_1(self):
        self.assertEqual(caesar_cipher("abc", 1), "bcd")

    def test_shift_26(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc")

    def test_with_special_characters(self):
        self.assertEqual(caesar_cipher("a!b@c", 1), "b!c@d")

    def test_uppercase_letters(self):
        self.assertEqual(caesar_cipher("ABC", 1), "BCD")

    def test_mixed_case_and_symbols(self):
        self.assertEqual(caesar_cipher("AbC!xYz", 2), "CdE!zAb")