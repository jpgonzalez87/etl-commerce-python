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

print("\n--- CUSTOMERS ---")
print(customers)

print("\n--- PRODUCTS ---")
print(products)

print("\n--- ORDERS ---")
print(orders)