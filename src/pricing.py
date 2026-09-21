"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 100 receive a 10-unit discount.
    
    Free shipping is applied when subtotal reaches 700, 900, 1000, or 1200.
    """
    discount_amount = 10 if subtotal >= 100 else 0
    free_shipping_700 = subtotal >= 700
    final_shipping = 0 if free_shipping_700 else shipping
    
    return {
        "subtotal": subtotal,
        "shipping": final_shipping,
        "discount_amount": discount_amount,
        "total": subtotal + final_shipping - discount_amount,
        "free_shipping_700": free_shipping_700,
        "free_shipping_900": subtotal >= 900,
        "free_shipping_1000": subtotal >= 1000,
        "free_shipping_1200": subtotal >= 1200,
    }
