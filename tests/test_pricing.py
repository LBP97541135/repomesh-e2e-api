import unittest

from src.pricing import calculate_quote


class PricingTest(unittest.TestCase):
    def test_regular_order(self):
        self.assertEqual(
            calculate_quote(80, 5),
            {"subtotal": 80, "shipping": 5, "total": 85},
        )


if __name__ == "__main__":
    unittest.main()
