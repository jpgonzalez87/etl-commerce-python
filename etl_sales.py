import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "data" / "output"

# Make sure output folder exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("BASE_DIR:", BASE_DIR)
print("RAW_DIR:", RAW_DIR)
print("OUTPUT_DIR:", OUTPUT_DIR)

# Extract
customers = pd.read_csv(RAW_DIR / "customers.csv")
products = pd.read_csv(RAW_DIR / "products.csv")
orders = pd.read_csv(RAW_DIR / "orders.csv")

# Transform: clean customers
customers["email"] = customers["email"].str.strip().str.lower()
customers["country"] = customers["country"].fillna("UNKNOWN")
customers["country"] = customers["country"].replace("", "UNKNOWN")
customers["country"] = customers["country"].str.upper()

# Transform: clean orders
orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")
orders = orders[orders["status"] == "completed"]
orders = orders[orders["product_id"].isin(products["product_id"])]

# Join tables
sales = orders.merge(customers, on="customer_id", how="inner")
sales = sales.merge(products, on="product_id", how="inner")

# Calculated column
sales["total_amount"] = sales["quantity"] * sales["price"]

# Final clean table
sales_clean = sales[
    [
        "order_id",
        "order_date",
        "customer_id",
        "name",
        "email",
        "country",
        "product_id",
        "product_name",
        "category",
        "quantity",
        "price",
        "total_amount",
    ]
].copy()

# Summary by country
country_summary = (
    sales_clean.groupby("country", as_index=False)
    .agg(
        total_orders=("order_id", "count"),
        total_revenue=("total_amount", "sum"),
    )
)

# Load / export
sales_clean.to_csv(OUTPUT_DIR / "sales_clean.csv", index=False)
country_summary.to_csv(OUTPUT_DIR / "country_summary.csv", index=False)

print("\n--- SALES CLEAN ---")
print(sales_clean)

print("\n--- COUNTRY SUMMARY ---")
print(country_summary)

print("\nFiles exported successfully to:", OUTPUT_DIR)