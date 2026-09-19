"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 100 receive a 10-unit discount."""
    discount_amount = 10 if subtotal >= 100 else 0
    
    # Free shipping when subtotal >= 1200
    if subtotal >= 1200:
        shipping = 0
    
    return {
        "subtotal": subtotal,
        "shipping": shipping,
        "discount_amount": discount_amount,
        "total": subtotal + shipping - discount_amount,
        "free_shipping_900": subtotal >= 900,
    }
