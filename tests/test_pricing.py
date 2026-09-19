import unittest

from src.pricing import calculate_quote


class PricingTest(unittest.TestCase):
    def test_regular_order(self):
        """Orders below the threshold receive no discount."""
        result = calculate_quote(80, 5)
        self.assertEqual(result["subtotal"], 80)
        self.assertEqual(result["shipping"], 5)
        self.assertEqual(result["discount_amount"], 0)
        self.assertEqual(result["total"], 85)
        self.assertFalse(result["free_shipping_900"])
        self.assertFalse(result["free_shipping_1500"])

    def test_threshold_order(self):
        """Orders at exactly the threshold (subtotal == 100) receive the discount."""
        result = calculate_quote(100, 5)
        self.assertEqual(result["subtotal"], 100)
        self.assertEqual(result["shipping"], 5)
        self.assertEqual(result["discount_amount"], 10)
        self.assertEqual(result["total"], 95)
        self.assertFalse(result["free_shipping_900"])
        self.assertFalse(result["free_shipping_1500"])

    def test_discount_applies_to_merchandise_only(self):
        """Discount is calculated from merchandise subtotal, not shipping."""
        result = calculate_quote(150, 20)
        self.assertEqual(result["discount_amount"], 10)
        # total = subtotal + shipping - discount_amount (shipping is not discounted)
        self.assertEqual(result["total"], 150 + 20 - 10)

    def test_free_shipping_at_1500(self):
        """When subtotal reaches 1500, shipping becomes 0."""
        result = calculate_quote(1500, 50)
        self.assertEqual(result["shipping"], 0)
        # total = subtotal + shipping(0) - discount(10) = 1490
        self.assertEqual(result["total"], 1490)

    def test_free_shipping_1500_field_true(self):
        """free_shipping_1500 returns True when subtotal >= 1500."""
        result = calculate_quote(1500, 50)
        self.assertTrue(result["free_shipping_1500"])

    def test_free_shipping_1500_field_false(self):
        """free_shipping_1500 returns False when subtotal < 1500."""
        result = calculate_quote(1499, 50)
        self.assertFalse(result["free_shipping_1500"])


if __name__ == "__main__":
    unittest.main()
