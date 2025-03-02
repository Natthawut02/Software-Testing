import unittest


def funnyString(s):
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            return "Not Funny"
    return "Funny"


class TestFunnyString(unittest.TestCase):
    def test_funny_string(self):
        self.assertEqual(funnyString("acxz"), "Funny")  # ผลต่างของ s และ r เท่ากัน
        self.assertEqual(funnyString("bcxz"), "Not Funny")  # ผลต่างของ s และ r ไม่เท่ากัน
        self.assertEqual(funnyString("abcd"), "Funny")  # ผลต่างของ s และ r เท่ากัน
        self.assertEqual(funnyString("aaaa"), "Funny")  # ทุกตัวอักษรเหมือนกัน ผลต่างเป็น 0
        self.assertEqual(funnyString("abba"), "Funny")  # ผลต่างของ s และ r เท่ากัน
        self.assertEqual(funnyString("ivvkxq"), "Not Funny")  # ผลต่างของ s และ r ไม่เท่ากัน
        self.assertEqual(funnyString("xxyy"), "Funny")  # ผลต่างของ s และ r เท่ากัน
        self.assertEqual(funnyString("ivvkx"), "Not Funny")  # ผลต่างของ s และ r ไม่เท่ากัน
        self.assertEqual(
            funnyString(
                "fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury"
            ),
            "Not Funny",
        )