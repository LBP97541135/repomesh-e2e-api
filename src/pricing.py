"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 100 receive a 10-unit discount.
    
    Shipping rules:
    - subtotal < 700: normal shipping fee, free_shipping_700 = False
    - subtotal >= 700: free shipping (shipping = 0), free_shipping_700 = True
    """
    discount_amount = 10 if subtotal >= 100 else 0
    
    # Apply free shipping for orders >= 700
    free_shipping_700 = subtotal >= 700
    final_shipping = 0 if free_shipping_700 else shipping
    
    return {
        "subtotal": subtotal,
        "shipping": final_shipping,
        "discount_amount": discount_amount,
        "total": subtotal + final_shipping - discount_amount,
        "free_shipping_700": free_shipping_700,
    }
