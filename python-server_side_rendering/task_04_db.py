#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)


def read_json():
    """Read products from JSON file."""
    with open("products.json", "r") as file:
        return json.load(file)


def read_csv():
    """Read products from CSV file."""
    with open("products.csv", "r") as file:
        return list(csv.DictReader(file))


def read_sql():
    """Read products from SQLite database."""
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")

    products = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return products


@app.route("/products")
def products():
    """Display products from JSON, CSV, or SQL."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv", "sql"]:
        return render_template(
            "product_display.html",
            error="Wrong source"
        )

    try:
        if source == "json":
            products_data = read_json()
        elif source == "csv":
            products_data = read_csv()
        else:
            products_data = read_sql()

    except sqlite3.Error:
        return render_template(
            "product_display.html",
            error="Database error"
        )

    if product_id:
        for product in products_data:
            if str(product["id"]) == product_id:
                return render_template(
                    "product_display.html",
                    products=[product]
                )

        return render_template(
            "product_display.html",
            error="Product not found"
        )

    return render_template(
        "product_display.html",
        products=products_data
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
