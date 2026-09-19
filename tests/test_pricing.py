import unittest

from src.pricing import calculate_quote


class PricingTest(unittest.TestCase):
    def test_regular_order(self):
        """Orders below the threshold receive no discount."""
        self.assertEqual(
            calculate_quote(80, 5),
            {"subtotal": 80, "shipping": 5, "discount_amount": 0, "total": 85, "free_shipping_1200": False},
        )

    def test_threshold_order(self):
        """Orders at exactly the threshold (subtotal == 100) receive the discount."""
        self.assertEqual(
            calculate_quote(100, 5),
            {"subtotal": 100, "shipping": 5, "discount_amount": 10, "total": 95, "free_shipping_1200": False},
        )

    def test_discount_applies_to_merchandise_only(self):
        """Discount is calculated from merchandise subtotal, not shipping."""
        result = calculate_quote(150, 20)
        self.assertEqual(result["discount_amount"], 10)
        # total = subtotal + shipping - discount_amount (shipping is not discounted)
        self.assertEqual(result["total"], 150 + 20 - 10)
        self.assertEqual(result["free_shipping_1200"], False)

    def test_subtotal_equal_to_1200(self):
        """Orders with subtotal exactly 1200 have shipping=0 and free_shipping_1200=True."""
        result = calculate_quote(1200, 100)
        self.assertEqual(result["shipping"], 0)
        self.assertEqual(result["free_shipping_1200"], True)

    def test_subtotal_greater_than_1200(self):
        """Orders with subtotal greater than 1200 have shipping=0 and free_shipping_1200=True."""
        result = calculate_quote(1500, 100)
        self.assertEqual(result["shipping"], 0)
        self.assertEqual(result["free_shipping_1200"], True)

    def test_subtotal_less_than_1200(self):
        """Orders with subtotal less than 1200 have shipping>0 and free_shipping_1200=False."""
        result = calculate_quote(800, 50)
        self.assertEqual(result["shipping"], 50)
        self.assertEqual(result["free_shipping_1200"], False)


if __name__ == "__main__":
    unittest.main()
