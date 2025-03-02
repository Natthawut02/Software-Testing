import unittest

def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))

    for col in range(len(grid[0])):
        for row in range(1, len(grid)):
            if grid[row][col] < grid[row - 1][col]:
                return "NO"
    return "YES"

import unittest




class TestGridChallenge(unittest.TestCase):
    def test_grid_challenge(self):
        test_cases = [
            (["abc", "ade", "efg"], "YES"),  # test 0
            (["uxf", "vof", "hmp"], "NO"),  # test 1
            (["lyivr", "uweor", "qxwyr", "uikjd"], "NO"),  # test 2
            (["a"], "YES"),
            (["zzzz", "yyyy", "xxxx", "wwww"], "NO"),
            (["abc", "defg", "hij"], "YES"),
            (["ebacd", "fghij", "olmkn", "trpqs", "xywuv"], "YES"),
            (["abcde", "fghij", "klmno", "pqrst", "uvwxy"], "YES"),
        ]

        for grid, expected in test_cases:
            with self.subTest(grid=grid):
                self.assertEqual(gridChallenge(grid), expected)

if __name__ == '__main__':
    unittest.main()
