import unittest
   
def cat_and_mouse(x, y, z):
    if abs(x - z) < abs(y - z):
        return "Cat A"
    elif abs(y - z) < abs(x - z):
        return "Cat B"
    return "Mouse C"

class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_wins(self):
        self.assertEqual(cat_and_mouse(1, 5, 2), "Cat A")

    def test_cat_b_wins(self):
        self.assertEqual(cat_and_mouse(2, 5, 4), "Cat B")

    def test_mouse_escapes(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")

    def test_equal_distance(self):
        self.assertEqual(cat_and_mouse(4, 6, 5), "Mouse C")

    def test_large_values(self):
        self.assertEqual(cat_and_mouse(10, 100, 50), "Cat A")