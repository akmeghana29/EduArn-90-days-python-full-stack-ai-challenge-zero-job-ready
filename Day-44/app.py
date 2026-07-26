"""
Product API (CRUD)
- GET    /products           - get all products
- GET    /products/<id>      - get one product
- POST   /products           - add a product
- PUT    /products/<id>      - update a product
- DELETE /products/<id>      - delete a product

Test with Postman or Thunder Client (VS Code extension)
"""

from flask import Flask, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)

FILE = "products.json"

# ---------- Load and Save ----------

def load():
    if Path(FILE).exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

# ---------- GET all products ----------

@app.route("/products", methods=["GET"])
def get_all():
    products = load()
    return jsonify({"total": len(products), "products": products}), 200

# ---------- GET one product ----------

@app.route("/products/<int:product_id>", methods=["GET"])
def get_one(product_id):
    products = load()
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# ---------- POST - add product ----------

@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name     = data.get("name", "").strip()
    price    = data.get("price")
    category = data.get("category", "").strip()
    stock    = data.get("stock")

    if not name or price is None or not category or stock is None:
        return jsonify({"error": "name, price, category and stock are required"}), 400

    if price < 0 or stock < 0:
        return jsonify({"error": "price and stock cannot be negative"}), 400

    products = load()
    new_id = max((p["id"] for p in products), default=0) + 1

    new_product = {
        "id": new_id,
        "name": name,
        "price": price,
        "category": category,
        "stock": stock
    }

    products.append(new_product)
    save(products)
    return jsonify({"message": "Product added", "product": new_product}), 201

# ---------- PUT - update product ----------

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    products = load()
    product = next((p for p in products if p["id"] == product_id), None)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    product["name"]     = data.get("name", product["name"])
    product["price"]    = data.get("price", product["price"])
    product["category"] = data.get("category", product["category"])
    product["stock"]    = data.get("stock", product["stock"])

    save(products)
    return jsonify({"message": "Product updated", "product": product}), 200

# ---------- DELETE product ----------

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    products = load()
    product = next((p for p in products if p["id"] == product_id), None)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    products.remove(product)
    save(products)
    return jsonify({"message": f"{product['name']} deleted"}), 200

# ---------- Run ----------

if __name__ == "__main__":
    app.run(debug=True)
