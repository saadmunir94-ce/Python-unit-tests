
import unittest
from rectangle import Rectangle
class TestGetAreaRectangleWithSetup(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # this method is only run once per the entire class rather than being run for each test which is done for the setUp()
        self.rectangle = Rectangle(1, 1)

    def test_normal_case(self):
        self.rectangle.height = 2
        self.rectangle.width = 3
        self.assertEqual(self.rectangle.get_area(), 6, "incorrect area")
    def test_negative_case(self):
        with self.assertRaises(ValueError):
            self.rectangle.width = -1