def caesarCipher(s, k):
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            result.append(chr(((ord(char) - ord('a') + k) % 26) + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr(((ord(char) - ord('A') + k) % 26) + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    fptr.close()






 # Test Case
import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")
        self.assertEqual(caesarCipher("abcdefghijklmnopqrstuvwxyz", 3), "defghijklmnopqrstuvwxyzabc")
        self.assertEqual(caesarCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3), "DEFGHIJKLMNOPQRSTUVWXYZABC")
        self.assertEqual(caesarCipher("There's-a-starman-waiting-in-the-sky", 3), "Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb")
        self.assertEqual(caesarCipher("123!@#", 5), "123!@#")
        self.assertEqual(caesarCipher("xyz", 5), "cde")
        self.assertEqual(caesarCipher("XYZ", 5), "CDE")
        self.assertEqual(caesarCipher("", 5), "")

if __name__ == '__main__':
    unittest.main()