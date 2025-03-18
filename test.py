import unittest
from calculator import add, subtract, multiply, divide, power, sqrt

class TestCalculator(unittest.TestCase):
    """
    Тесты для функций калькулятора.
    """

    def test_add(self):
        """
        Тестирование функции сложения.
        """
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """
        Тестирование функции вычитания.
        """
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        """
        Тестирование функции умножения.
        """
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        """
        Тестирование функции деления.
        """
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(0, 5), 0)

        # Проверка деления на ноль
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_power(self):
        """
        Тестирование функции возведения в степень.
        """
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(-2, 2), 4)
        self.assertEqual(power(-2, 3), -8)

    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(9), 3)
        with self.assertRaises(ValueError):
            sqrt(-1)
if __name__ == "__main__":
    unittest.main()