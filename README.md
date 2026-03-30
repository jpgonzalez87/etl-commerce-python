# ETL Commerce Python

A small ETL practice project built with **Python** and **pandas**.

This project was created as part of my learning journey as a Business Analyst who is gradually expanding into data analysis and data engineering. The goal was not to build something overly complex, but to understand the ETL flow end to end in a practical and approachable way.

---

## Project overview

This script reads raw CSV files, cleans and transforms the data, joins related datasets, calculates sales totals, and exports analysis-ready output files.

It follows a simple ETL structure:

| Step | What it does |
|------|----------------|
| **Extract** | Read raw input files |
| **Transform** | Clean, filter, join, and enrich data |
| **Load** | Export final datasets for analysis |

---

## Why I built this

As a BA, I have worked closely with data, reporting, product decisions, and cross-functional teams for years. Recently, I started dedicating time to strengthen the more hands-on side of that work through Python and small data exercises like this one.

This project is intentionally simple. That is part of the point.

It helped me practice:

- reading and understanding raw datasets
- cleaning inconsistent values
- joining related tables
- calculating derived metrics
- exporting clean outputs
- structuring a small project in a more maintainable way
- versioning the work step by step with Git and GitHub

---

## Project structure

```text
etl-commerce-python/
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── orders.csv
│   │   └── products.csv
│   └── output/
├── etl_sales.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Input files

The script expects these input files inside `data/raw/`:

| File | Role |
|------|------|
| `customers.csv` | Customer master data |
| `products.csv` | Product catalog |
| `orders.csv` | Order lines |

These files contain sample e-commerce data with a few intentional inconsistencies, such as:

- emails with extra spaces or uppercase letters
- missing country values
- cancelled orders
- product references that do not exist in the product table

---

## Transformation logic

The ETL process currently applies the following rules.

### Customers

- Trim spaces from `email`
- Convert `email` to lowercase
- Replace missing or empty `country` values with `UNKNOWN`
- Convert `country` to uppercase

### Orders

- Convert `order_date` to a date format
- Keep only orders with `status = completed`
- Remove orders with invalid `product_id` values

### Final dataset

- Join orders with customers on `customer_id`
- Join the result with products on `product_id`
- Add column: `total_amount = quantity * price`

### Summary output

- Group sales by `country`
- Calculate:
  - `total_orders`
  - `total_revenue`

---

## Output files

The script generates these files inside `data/output/`:

| File | Contents |
|------|----------|
| `sales_clean.csv` | Clean, joined sales rows |
| `country_summary.csv` | Aggregates by country |

These output files are intentionally ignored by Git, since they are generated artifacts rather than source files.

---

## Tech used

- **Python**
- **pandas**
- **Git** & **GitHub**

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the project

```bash
python etl_sales.py
```

---

## Expected result

The script should:

- generate a clean sales file with valid completed orders
- generate a country-level summary of total orders and revenue
- export both files to `data/output/`

For the sample data currently included in the project, the expected summary is:

| Country | Orders | Revenue |
|---------|--------|---------|
| AR | 1 | 300 |
| UY | 3 | 1325 |

---

## Notes

One small but useful detail in this project is that output CSV files are exported using **`utf-8-sig`** encoding so they open correctly in **Excel on Windows**, especially when names contain accented characters.

---

## Final thought

This is a small learning project, but a meaningful one for me.

It reflects the kind of growth I am currently pursuing: expanding my BA toolkit with more practical data skills, step by step, with curiosity and consistency.

I hope it can also be helpful for other BAs or professionals who are exploring a similar path.
