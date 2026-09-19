import unittest

from src.pricing import calculate_quote


class PricingTest(unittest.TestCase):
    def test_regular_order(self):
        """Orders below the threshold receive no discount."""
        self.assertEqual(
            calculate_quote(80, 5),
            {"subtotal": 80, "shipping": 5, "discount_amount": 0, "total": 85, "free_shipping_700": False},
        )

    def test_threshold_order(self):
        """Orders at exactly the threshold (subtotal == 100) receive the discount."""
        self.assertEqual(
            calculate_quote(100, 5),
            {"subtotal": 100, "shipping": 5, "discount_amount": 10, "total": 95, "free_shipping_700": False},
        )

    def test_discount_applies_to_merchandise_only(self):
        """Discount is calculated from merchandise subtotal, not shipping."""
        result = calculate_quote(150, 20)
        self.assertEqual(result["discount_amount"], 10)
        # total = subtotal + shipping - discount_amount (shipping is not discounted)
        self.assertEqual(result["total"], 150 + 20 - 10)
        self.assertEqual(result["free_shipping_700"], False)

    def test_shipping_below_700(self):
        """Subtotal < 700: normal shipping fee, free_shipping_700 = False."""
        result = calculate_quote(699, 15)
        self.assertEqual(result["shipping"], 15)
        self.assertEqual(result["free_shipping_700"], False)
        # subtotal >= 100, so discount applies
        self.assertEqual(result["total"], 699 + 15 - 10)

    def test_shipping_at_700(self):
        """Subtotal >= 700: free shipping (shipping = 0), free_shipping_700 = True."""
        result = calculate_quote(700, 15)
        self.assertEqual(result["shipping"], 0)
        self.assertEqual(result["free_shipping_700"], True)
        # subtotal >= 100, so discount applies; shipping is 0
        self.assertEqual(result["total"], 700 - 10)

    def test_shipping_above_700(self):
        """Subtotal > 700: free shipping, free_shipping_700 = True."""
        result = calculate_quote(1000, 20)
        self.assertEqual(result["shipping"], 0)
        self.assertEqual(result["free_shipping_700"], True)
        # subtotal >= 100, so discount applies; shipping is 0
        self.assertEqual(result["total"], 1000 - 10)

    def test_free_shipping_with_discount(self):
        """Free shipping applies even when discount is also applied."""
        result = calculate_quote(700, 25)
        self.assertEqual(result["discount_amount"], 10)  # >= 100 gets discount
        self.assertEqual(result["shipping"], 0)  # but shipping is free
        self.assertEqual(result["free_shipping_700"], True)
        self.assertEqual(result["total"], 700 - 10)  # subtotal - discount

    def test_free_shipping_700_boundary(self):
        """Verify exact boundary: 699 vs 700."""
        # 699: not free shipping
        result_699 = calculate_quote(699, 10)
        self.assertFalse(result_699["free_shipping_700"])
        self.assertEqual(result_699["shipping"], 10)
        
        # 700: free shipping
        result_700 = calculate_quote(700, 10)
        self.assertTrue(result_700["free_shipping_700"])
        self.assertEqual(result_700["shipping"], 0)


if __name__ == "__main__":
    unittest.main()
