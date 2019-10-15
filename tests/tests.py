import unittest
import math

from homework import Rectangle


class RectangleTest(unittest.TestCase):

    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.rect.get_rectangle_perimeter(), 8)

    def setUp(self):
        self.rect = Rectangle(2, 2)
        self.rect1 = Rectangle(3, 2)

    def tearDown(self):
        pass

    def test_rectangle_square(self):
        self.assertEqual(self.rect.get_rectangle_square(), 4)

    def test_get_sum_of_corner(self):
        number_of_corners = [0, 1, 2, 3, 4]
        sum_of_corner = [0, 90, 180, 270, 360]
        for i in range(len(number_of_corners)):
            with self.subTest(i=i):
                self.assertEqual(self.rect.get_sum_of_corners(i), sum_of_corner[i])

    def test_get_rectangle_diagonal(self):
        for i in range(2, 10):
            dia = math.sqrt(math.pow(i, 2) + math.pow(i, 2))
            self.rect = Rectangle(i, i)
            with self.subTest(i=i):
                self.assertEqual(self.rect.get_rectangle_diagonal(), dia)

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.rect.get_radius_of_circumscribed_circle(), (self.rect.get_rectangle_diagonal()) / 2)

    def test_get_radius_of_inscribed_circle(self):
        self.assertEqual(self.rect.get_radius_of_inscribed_circle(), self.rect.get_rectangle_diagonal() / (2 * math.sqrt(2)))
        self.assertRaises(ValueError, self.rect1.get_radius_of_inscribed_circle)


if __name__ == "__main__":
    unittest.main()
