#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


def read_json():
    """Read products from JSON file."""
    with open("products.json", "r") as file:
        return json.load(file)


def read_csv():
    """Read products from CSV file."""
    with open("products.csv", "r") as file:
        return list(csv.DictReader(file))


@app.route("/products")
def products():
    """Display products from JSON or CSV."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template(
            "product_display.html",
            error="Wrong source"
        )

    if source == "json":
        products_data = read_json()
    else:
        products_data = read_csv()

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
