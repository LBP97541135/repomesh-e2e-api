"""Pricing API used by the RepoMesh delivery acceptance test."""


def calculate_quote(subtotal: int, shipping: int) -> dict[str, int]:
    """Return a checkout quote; orders of at least 100 receive a 10-unit discount."""
    discount = 10 if subtotal >= 100 else 0
    return {
        "subtotal": subtotal,
        "shipping": shipping,
        "total": subtotal + shipping - discount,
    }
