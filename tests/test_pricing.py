import unittest

from src.pricing import calculate_quote


class PricingTest(unittest.TestCase):
    def test_regular_order(self):
        """Orders below the threshold receive no discount."""
        self.assertEqual(
            calculate_quote(10, 5),
            {"subtotal": 10, "shipping": 5, "discount_amount": 0, "total": 15},
        )

    def test_threshold_order(self):
        """Orders at exactly the threshold (subtotal == 11) receive the discount."""
        self.assertEqual(
            calculate_quote(11, 5),
            {"subtotal": 11, "shipping": 5, "discount_amount": 11, "total": 5},
        )

    def test_discount_applies_to_merchandise_only(self):
        """Discount is calculated from merchandise subtotal, not shipping."""
        result = calculate_quote(20, 20)
        self.assertEqual(result["discount_amount"], 11)
        # total = subtotal + shipping - discount_amount (shipping is not discounted)
        self.assertEqual(result["total"], 20 + 20 - 11)


if __name__ == "__main__":
    unittest.main()
