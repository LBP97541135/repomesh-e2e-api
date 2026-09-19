"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 100 receive a 10-unit discount.
    
    Orders of at least 200 receive free shipping.
    """
    discount_amount = 10 if subtotal >= 100 else 0
    
    # Free shipping for orders with subtotal >= 200
    free_shipping_200 = subtotal >= 200
    actual_shipping = 0 if free_shipping_200 else shipping
    
    return {
        "subtotal": subtotal,
        "shipping": actual_shipping,
        "discount_amount": discount_amount,
        "free_shipping_200": free_shipping_200,
        "total": subtotal + actual_shipping - discount_amount,
    }
