"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 100 receive a 10-unit discount.
    
    Orders of at least 500 subtotal receive free shipping.
    """
    discount_amount = 10 if subtotal >= 100 else 0
    free_shipping = subtotal >= 500
    final_shipping = 0 if free_shipping else shipping
    return {
        "subtotal": subtotal,
        "shipping": final_shipping,
        "discount_amount": discount_amount,
        "free_shipping": free_shipping,
        "total": subtotal + final_shipping - discount_amount,
    }
