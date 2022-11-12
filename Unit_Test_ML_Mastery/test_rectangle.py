import unittest
from rectangle import Rectangle
class TestGetAreaRectangle(unittest.TestCase):
    def test_normal_case(self):
        # override runTest method
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "area should be 6")
    def test_negative_case(self):
        # a dummy example indeed
        """expect -1 as output to denote error when looking at negative area"""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-1, 2)
        #self.assertGreaterEqual(rectangle.get_area(), -1, "incorrect negative output")