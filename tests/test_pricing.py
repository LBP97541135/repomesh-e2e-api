import unittest

from src.pricing import calculate_quote


class PricingTest(unittest.TestCase):
    def test_regular_order(self):
        """Orders below the threshold receive no discount."""
        self.assertEqual(
            calculate_quote(80, 5),
            {"subtotal": 80, "shipping": 5, "discount_amount": 0, "free_shipping_200": False, "total": 85},
        )

    def test_threshold_order(self):
        """Orders at exactly the threshold (subtotal == 100) receive the discount."""
        self.assertEqual(
            calculate_quote(100, 5),
            {"subtotal": 100, "shipping": 5, "discount_amount": 10, "free_shipping_200": False, "total": 95},
        )

    def test_discount_applies_to_merchandise_only(self):
        """Discount is calculated from merchandise subtotal, not shipping."""
        result = calculate_quote(150, 20)
        self.assertEqual(result["discount_amount"], 10)
        # total = subtotal + shipping - discount_amount (shipping is not discounted)
        self.assertEqual(result["total"], 150 + 20 - 10)

    def test_free_shipping_at_200(self):
        """Orders with subtotal >= 200 receive free shipping and discount."""
        result = calculate_quote(200, 10)
        self.assertEqual(result["free_shipping_200"], True)
        self.assertEqual(result["shipping"], 0)
        self.assertEqual(result["discount_amount"], 10)
        # total = subtotal + shipping (0) - discount_amount
        self.assertEqual(result["total"], 200 - 10)

    def test_free_shipping_above_200(self):
        """Orders with subtotal > 200 also receive free shipping and discount."""
        result = calculate_quote(250, 15)
        self.assertEqual(result["free_shipping_200"], True)
        self.assertEqual(result["shipping"], 0)
        self.assertEqual(result["discount_amount"], 10)
        self.assertEqual(result["total"], 250 - 10)


if __name__ == "__main__":
    unittest.main()
