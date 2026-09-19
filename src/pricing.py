"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 300 receive a 30-unit discount."""
    discount_amount = 30 if subtotal >= 300 else 0
    return {
        "subtotal": subtotal,
        "shipping": shipping,
        "discount_amount": discount_amount,
        "total": subtotal + shipping - discount_amount,
    }
