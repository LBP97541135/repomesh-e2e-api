import unittest

from src.pricing import calculate_quote


class PricingTest(unittest.TestCase):
    def test_regular_order(self):
        """Orders below the threshold receive no discount."""
        self.assertEqual(
            calculate_quote(80, 5),
            {"subtotal": 80, "shipping": 5, "discount_amount": 0, "free_shipping": False, "total": 85},
        )

    def test_threshold_order(self):
        """Orders at exactly the threshold (subtotal == 100) receive the discount."""
        self.assertEqual(
            calculate_quote(100, 5),
            {"subtotal": 100, "shipping": 5, "discount_amount": 10, "free_shipping": False, "total": 95},
        )

    def test_discount_applies_to_merchandise_only(self):
        """Discount is calculated from merchandise subtotal, not shipping."""
        result = calculate_quote(150, 20)
        self.assertEqual(result["discount_amount"], 10)
        # total = subtotal + shipping - discount_amount (shipping is not discounted)
        self.assertEqual(result["total"], 150 + 20 - 10)

    def test_free_shipping_threshold(self):
        """Orders with subtotal >= 500 receive free shipping (and discount if >= 100)."""
        result = calculate_quote(500, 20)
        self.assertEqual(result["shipping"], 0)
        self.assertEqual(result["free_shipping"], True)
        # subtotal >= 100 gets 10 discount, shipping is 0
        self.assertEqual(result["total"], 500 - 10)

    def test_free_shipping_above_threshold(self):
        """Orders with subtotal > 500 also receive free shipping."""
        result = calculate_quote(600, 15)
        self.assertEqual(result["shipping"], 0)
        self.assertEqual(result["free_shipping"], True)
        # subtotal >= 100 gets 10 discount, shipping is 0
        self.assertEqual(result["total"], 600 - 10)

    def test_free_shipping_below_threshold(self):
        """Orders with subtotal < 500 do not receive free shipping (but may get discount)."""
        result = calculate_quote(499, 25)
        self.assertEqual(result["shipping"], 25)
        self.assertEqual(result["free_shipping"], False)
        # subtotal >= 100 gets 10 discount
        self.assertEqual(result["total"], 499 + 25 - 10)


if __name__ == "__main__":
    unittest.main()
