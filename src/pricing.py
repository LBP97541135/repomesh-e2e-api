"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 300 receive a 30-unit discount."""
    discount = 30 if subtotal >= 300 else 0
    return {
        "subtotal": subtotal,
        "shipping": shipping,
        "discount": discount,
        "total": subtotal + shipping - discount,
    }
