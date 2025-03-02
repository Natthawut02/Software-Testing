def alternatingCharacters(s):
alternatingCharacters    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()



# Test Cases
    def test_alternating_characters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)
        self.assertEqual(alternatingCharacters("AAABBB"), 4)
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("AB"), 0)
        self.assertEqual(alternatingCharacters("ABA"), 0)
        self.assertEqual(alternatingCharacters("ABAB"), 0)
        self.assertEqual(alternatingCharacters("ABABBB"), 1)

if __name__ == '__main__':
    unittest.main()