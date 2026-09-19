"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 100 receive a 10-unit discount.
    
    Free shipping is applied when subtotal reaches 700.
    """
    discount_amount = 10 if subtotal >= 100 else 0
    # Free shipping when subtotal >= 700
    shipping_fee = 0 if subtotal >= 700 else shipping
    return {
        "subtotal": subtotal,
        "shipping": shipping_fee,
        "discount_amount": discount_amount,
        "total": subtotal + shipping_fee - discount_amount,
    }
