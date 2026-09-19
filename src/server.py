"""API server for RepoMesh end-to-end delivery validation."""

import os
from flask import Flask, jsonify, request

from pricing import calculate_quote

__version__ = "1.0.0"

app = Flask(__name__)


@app.route("/healthz")
def healthz():
    """Health check endpoint that returns version information."""
    return jsonify({
        "status": "healthy",
        "version": __version__
    })


@app.route("/api/quote", methods=["POST"])
def quote():
    """Calculate checkout quote."""
    subtotal = request.json.get("subtotal", 0)
    shipping = request.json.get("shipping", 0)
    return jsonify(calculate_quote(subtotal, shipping))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
