import unittest

from src.pricing import calculate_quote


class PricingTest(unittest.TestCase):
    def test_regular_order(self):
        """Orders below the threshold receive no discount."""
        self.assertEqual(
            calculate_quote(80, 5),
            {
                "subtotal": 80,
                "shipping": 5,
                "discount_amount": 0,
                "total": 85,
                "free_shipping_900": False,
                "free_shipping_1200": False,
            },
        )

    def test_threshold_order(self):
        """Orders at exactly the threshold (subtotal == 100) receive the discount."""
        self.assertEqual(
            calculate_quote(100, 5),
            {
                "subtotal": 100,
                "shipping": 5,
                "discount_amount": 10,
                "total": 95,
                "free_shipping_900": False,
                "free_shipping_1200": False,
            },
        )

    def test_discount_applies_to_merchandise_only(self):
        """Discount is calculated from merchandise subtotal, not shipping."""
        result = calculate_quote(150, 20)
        self.assertEqual(result["discount_amount"], 10)
        # total = subtotal + shipping - discount_amount (shipping is not discounted)
        self.assertEqual(result["total"], 150 + 20 - 10)
        self.assertEqual(result["free_shipping_900"], False)
        self.assertEqual(result["free_shipping_1200"], False)

    def test_free_shipping_900(self):
        """Orders with subtotal >= 900 qualify for free_shipping_900."""
        result = calculate_quote(900, 50)
        self.assertEqual(result["free_shipping_900"], True)
        self.assertEqual(result["free_shipping_1200"], False)
        self.assertEqual(result["shipping"], 50)  # shipping still applies at 900

    def test_free_shipping_1200(self):
        """Orders with subtotal >= 1200 get free shipping (plus discount if >= 100)."""
        result = calculate_quote(1200, 50)
        self.assertEqual(result["free_shipping_900"], True)
        self.assertEqual(result["free_shipping_1200"], True)
        self.assertEqual(result["shipping"], 0)  # shipping is waived
        # total = subtotal + 0 - discount (discount also applies since 1200 >= 100)
        self.assertEqual(result["total"], 1190)

    def test_free_shipping_1200_above_threshold(self):
        """Orders well above 1200 also get free shipping."""
        result = calculate_quote(1500, 30)
        self.assertEqual(result["free_shipping_1200"], True)
        self.assertEqual(result["shipping"], 0)
        # discount also applies since 1500 >= 100
        self.assertEqual(result["total"], 1490)

    def test_free_shipping_1200_below_threshold(self):
        """Orders below 1200 do not get free shipping even at 1199."""
        result = calculate_quote(1199, 25)
        self.assertEqual(result["free_shipping_1200"], False)
        self.assertEqual(result["shipping"], 25)


if __name__ == "__main__":
    unittest.main()
