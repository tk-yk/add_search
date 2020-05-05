import unittest


def add(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x,y):
    return x / y


class TestCaliculation(unittest.TestCase):
    def test_二つの整数の和を計算できる(self):
        self.assertEqual(7, add(3, 4))

    def test_二つの整数のさを計算できる(self):
        self.assertEqual(1, subtraction(5, 4))

    def test_二つの整数の積を計算できる(self):
        self.assertEqual(6, multiplication(2, 3))

    def test_二つの整数の徐を計算できる(self):
        self.assertEqual(6, division(12, 2))


if __name__ == '__main__':
    unittest.main()
