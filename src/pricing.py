"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 100 receive a 10-unit discount."""
    discount_amount = 10 if subtotal >= 100 else 0
    # Free shipping when subtotal >= 1500
    final_shipping = 0 if subtotal >= 1500 else shipping
    return {
        "subtotal": subtotal,
        "shipping": final_shipping,
        "discount_amount": discount_amount,
        "total": subtotal + final_shipping - discount_amount,
        "free_shipping_900": subtotal >= 900,
        "free_shipping_1500": subtotal >= 1500,
    }
