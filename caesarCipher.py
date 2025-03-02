import unittest
import io
import sys
from unittest.mock import patch

def caesarCipher(s, k):
    result = []
    k = k % 26  
    for char in s:
        if 'a' <= char <= 'z':
            result.append(chr(((ord(char) - ord('a') + k) % 26) + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr(((ord(char) - ord('A') + k) % 26) + ord('A')))
        else:
            result.append(char)
    return ''.join(result)
    
def main():
    import os
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w') 
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    fptr.close()

# Test Cases
class TestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher(self):
        test_cases = [
            ("middle-Outz", 2, "okffng-Qwvb"),
            ("abcdefghijklmnopqrstuvwxyz", 3, "defghijklmnopqrstuvwxyzabc"),
            ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3, "DEFGHIJKLMNOPQRSTUVWXYZABC"),
            ("There's-a-starman-waiting-in-the-sky", 3, "Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb"),
            ("123!@#", 5, "123!@#"),
            ("xyz", 5, "cde"),
            ("XYZ", 5, "CDE"),
            ("", 5, ""),
            ("Hello, World!", 7, "Olssv, Dvysk!"),
            ("rotate-me-by-26", 26, "rotate-me-by-26"),
        ]

        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k):
                self.assertEqual(caesarCipher(s, k), expected)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['5', 'Hello', '3'])
    @patch('builtins.open')
    def test_main_function(self, mock_open, mock_input, mock_stdout):

        mock_file = mock_open.return_value
        main()

        mock_file.write.assert_called_once_with('Khoor\n')
        mock_file.close.assert_called_once()
    @patch('unittest.main')
    def test_main_execution(self, mock_unittest_main):
        original_name = __name__
        
        try:
            globals()['__name__'] = '__main__'
            exec(open(__file__).read())
            mock_unittest_main.assert_called_once()
        finally:
            globals()['__name__'] = original_name

if __name__ == '__main__':
    unittest.main()