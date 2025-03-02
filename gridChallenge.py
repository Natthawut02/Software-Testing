def gridChallenge(grid):
    # Sort each row alphabetically
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))
    
    # Check if columns are sorted
    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"
    return "YES"



    

 # Test Case
import unittest

class TestGridChallenge(unittest.TestCase):
    def test_grid_challenge(self):
        self.assertEqual(gridChallenge(["abc", "ade", "efg"]), "YES")
        self.assertEqual(gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES")
        self.assertEqual(gridChallenge(["mpxz", "abcd", "wlmf"]), "NO")
        self.assertEqual(gridChallenge(["abc", "hjk", "mpq", "rtv"]), "YES")
        self.assertEqual(gridChallenge(["a"]), "YES")
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")
        self.assertEqual(gridChallenge(["xyz", "abc", "def"]), "NO")
        self.assertEqual(gridChallenge(["zzz", "zzz", "zzz"]), "YES")
        self.assertEqual(gridChallenge(["zzz", "aaa", "bbb"]), "NO")

if __name__ == '__main__':
    unittest.main()