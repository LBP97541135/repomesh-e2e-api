"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 1200 receive free shipping."""
    free_shipping_threshold = 1200
    free_shipping = subtotal >= free_shipping_threshold
    shipping_cost = 0 if free_shipping else shipping
    discount_amount = 10 if subtotal >= 100 else 0
    return {
        "subtotal": subtotal,
        "shipping": shipping_cost,
        "discount_amount": discount_amount,
        "total": subtotal + shipping_cost - discount_amount,
        "free_shipping_1200": free_shipping,
    }
