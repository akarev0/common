import unittest
import math

from .homework import Rectangle


class RectangleTest(unittest.TestCase):

    def test_get_rectangle_perimeter(self):
        rect = self.rect_instance()
        self.assertEqual(rect.get_rectangle_perimeter(), 8)

    def rect_instance(self):
        rect = Rectangle(2, 2)
        return rect

    def test_rectangle_square(self):
        rect = self.rect_instance()
        self.assertEqual(rect.get_rectangle_square(), 4)

    def test_get_sum_of_corner(self):
        rect = self.rect_instance()
        number_of_corners = [0, 1, 2, 3, 4]
        sum_of_corner = [0, 90, 180, 270, 360]
        for i in range(len(number_of_corners)):
            self.assertEqual(rect.get_sum_of_corners(i), sum_of_corner[i])

    def test_get_rectangle_diagonal(self):
        rect = self.rect_instance()
        for i in range(2, 2):
            dia = math.sqrt(math.pow(i, 2) + math.pow(i, 2))
            self.assertEqual(rect.get_rectangle_diagonal(), dia)

    def test_get_radius_of_circumscribed_circle(self):
        rect = self.rect_instance()
        self.assertEqual(rect.get_radius_of_circumscribed_circle(), (rect.get_rectangle_diagonal()) / 2)

    def test_get_radius_of_inscribed_circle(self):
        rect = self.rect_instance()
        self.assertEqual(rect.get_radius_of_inscribed_circle(), rect.get_rectangle_diagonal() / (2 * math.sqrt(2)))
        self.assertRaises(ValueError, rect.get_radius_of_circumscribed_circle())


if __name__ == "__main__":
    unittest.main()
