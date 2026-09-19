import unittest

from src.pricing import calculate_quote


class PricingTest(unittest.TestCase):
    def test_regular_order(self):
        """Orders below the threshold receive no discount."""
        self.assertEqual(
            calculate_quote(80, 5),
            {"subtotal": 80, "shipping": 5, "discount": 0, "total": 85},
        )

    def test_threshold_order(self):
        """Orders at exactly the threshold (subtotal == 300) receive the discount."""
        self.assertEqual(
            calculate_quote(300, 5),
            {"subtotal": 300, "shipping": 5, "discount": 30, "total": 275},
        )

    def test_discount_applies_to_merchandise_only(self):
        """Discount is calculated from merchandise subtotal, not shipping."""
        result = calculate_quote(350, 20)
        self.assertEqual(result["discount"], 30)
        # total = subtotal + shipping - discount (shipping is not discounted)
        self.assertEqual(result["total"], 350 + 20 - 30)


if __name__ == "__main__":
    unittest.main()
