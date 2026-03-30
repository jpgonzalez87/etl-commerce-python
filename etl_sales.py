import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR = BASE_DIR / "data" / "output"

print("BASE_DIR:", BASE_DIR)
print("RAW_DIR:", RAW_DIR)
print("OUTPUT_DIR:", OUTPUT_DIR)

# Extract
customers = pd.read_csv(RAW_DIR / "customers.csv")
products = pd.read_csv(RAW_DIR / "products.csv")
orders = pd.read_csv(RAW_DIR / "orders.csv")

print("\n--- CUSTOMERS ORIGINAL ---")
print(customers)

# Transform: clean customers
customers["email"] = customers["email"].str.strip().str.lower()
customers["country"] = customers["country"].fillna("UNKNOWN")
customers["country"] = customers["country"].replace("", "UNKNOWN")
customers["country"] = customers["country"].str.upper()

print("\n--- CUSTOMERS CLEAN ---")
print(customers)

print("\n--- PRODUCTS ---")
print(products)

print("\n--- ORDERS ORIGINAL ---")
print(orders)

# Transform: clean orders
orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")
orders = orders[orders["status"] == "completed"]
orders = orders[orders["product_id"].isin(products["product_id"])]

print("\n--- ORDERS CLEAN ---")
print(orders)

# Join 1: orders + customers
sales = orders.merge(customers, on="customer_id", how="inner")

print("\n--- SALES AFTER JOIN WITH CUSTOMERS ---")
print(sales)

# Join 2: sales + products
sales = sales.merge(products, on="product_id", how="inner")

print("\n--- SALES AFTER JOIN WITH PRODUCTS ---")
print(sales)

# Calculated column
sales["total_amount"] = sales["quantity"] * sales["price"]

print("\n--- SALES WITH TOTAL AMOUNT ---")
print(sales)