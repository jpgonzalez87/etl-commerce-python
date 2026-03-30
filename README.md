# ETL Commerce Python

A small ETL practice project built with Python and pandas.

This project was created as part of my learning journey as a Business Analyst who is gradually expanding into data analysis and data engineering. The goal was not to build something overly complex, but to understand the ETL flow end to end in a practical and approachable way.

## Project overview

This script reads raw CSV files, cleans and transforms the data, joins related datasets, calculates sales totals, and exports analysis-ready output files.

It follows a simple ETL structure:

- **Extract**: read raw input files
- **Transform**: clean, filter, join, and enrich data
- **Load**: export final datasets for analysis

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

## Input files

The script expects these input files inside data/raw/:

- customers.csv
- products.csv
- orders.csv

These files contain sample e-commerce data with a few intentional inconsistencies, such as:

- emails with extra spaces or uppercase letters
- missing country values
- cancelled orders
- product references that do not exist in the product table

## Transformation logic

The ETL process currently applies the following rules:

Customers

- trims spaces from email
- converts email to lowercase
- replaces missing or empty country values with UNKNOWN
- converts country to uppercase

Orders

- converts order_date to a date format
- keeps only orders with status = completed
- removes orders with invalid product_id values

Final dataset

- joins orders with customers using customer_id
- joins the result with products using product_id
- creates a new column: total_amount = quantity * price

Summary output

- groups sales by country
- calculates:
- total_orders
- total_revenue

## Output files

The script generates these files inside data/output/:

- sales_clean.csv
- country_summary.csv

These output files are intentionally ignored by Git, since they are generated artifacts rather than source files.

## Tech used

- Python
- pandas
- Git
- GitHub

## Install dependencies

- `pip install -r requirements.txt`

## Run the project

- `python etl_sales.py`

## Expected result

The script should:

- generate a clean sales file with valid completed orders
- generate a country-level summary of total orders and revenue
- export both files to data/output/

For the sample data currently included in the project, the expected summary is:

- AR → 1 order → 300 revenue
- UY → 3 orders → 1325 revenue

## Notes

- One small but useful detail in this project is that output CSV files are exported using utf-8-sig encoding so they open correctly in Excel on Windows, especially when names contain accented characters.

## Final thought

- This is a small learning project, but a meaningful one for me.
- It reflects the kind of growth I am currently pursuing: expanding my BA toolkit with more practical data skills, step by step, with curiosity and consistency.
- I hope it can also be helpful for other BAs or professionals who are exploring a similar path.
# ETL Commerce Python

A small ETL practice project built with Python and pandas.

This project was created as part of my learning journey as a Business Analyst who is gradually expanding into data analysis and data engineering. The goal was not to build something overly complex, but to understand the ETL flow end to end in a practical and approachable way.

## Project overview

This script reads raw CSV files, cleans and transforms the data, joins related datasets, calculates sales totals, and exports analysis-ready output files.

It follows a simple ETL structure:

- **Extract**: read raw input files
- **Transform**: clean, filter, join, and enrich data
- **Load**: export final datasets for analysis

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
<<<<<<< HEAD

## Input files

The script expects these input files inside `data/raw/`:

- `customers.csv`
- `products.csv`
- `orders.csv`
=======
```

## Input files

The script expects these input files inside data/raw/:

- customers.csv
- products.csv
- orders.csv
>>>>>>> d7927d3 (Update README with project overview and usage instructions)

These files contain sample e-commerce data with a few intentional inconsistencies, such as:

- emails with extra spaces or uppercase letters
- missing country values
- cancelled orders
- product references that do not exist in the product table

## Transformation logic

The ETL process currently applies the following rules:

<<<<<<< HEAD
### Customers

- trims spaces from `email`
- converts `email` to lowercase
- replaces missing or empty `country` values with `UNKNOWN`
- converts `country` to uppercase

### Orders

- converts `order_date` to a date format
- keeps only orders with `status = completed`
- removes orders with invalid `product_id` values

### Final dataset

- joins orders with customers using `customer_id`
- joins the result with products using `product_id`
- creates a new column: `total_amount = quantity * price`

### Summary output

- groups sales by country
- calculates:
  - `total_orders`
  - `total_revenue`

## Output files

The script generates these files inside `data/output/`:

- `sales_clean.csv`
- `country_summary.csv`
=======
Customers

- trims spaces from email
- converts email to lowercase
- replaces missing or empty country values with UNKNOWN
- converts country to uppercase

Orders

- converts order_date to a date format
- keeps only orders with status = completed
- removes orders with invalid product_id values

Final dataset

- joins orders with customers using customer_id
- joins the result with products using product_id
- creates a new column: total_amount = quantity * price

Summary output

- groups sales by country
- calculates:
- total_orders
- total_revenue

## Output files

The script generates these files inside data/output/:

- sales_clean.csv
- country_summary.csv
>>>>>>> d7927d3 (Update README with project overview and usage instructions)

These output files are intentionally ignored by Git, since they are generated artifacts rather than source files.

## Tech used

- Python
- pandas
- Git
- GitHub

## Install dependencies

<<<<<<< HEAD
```bash
pip install -r requirements.txt

=======
- `pip install -r requirements.txt`

## Run the project

- `python etl_sales.py`

## Expected result

The script should:

- generate a clean sales file with valid completed orders
- generate a country-level summary of total orders and revenue
- export both files to data/output/

For the sample data currently included in the project, the expected summary is:

- AR → 1 order → 300 revenue
- UY → 3 orders → 1325 revenue

## Notes

- One small but useful detail in this project is that output CSV files are exported using utf-8-sig encoding so they open correctly in Excel on Windows, especially when names contain accented characters.

## Final thought

- This is a small learning project, but a meaningful one for me.

- It reflects the kind of growth I am currently pursuing: expanding my BA toolkit with more practical data skills, step by step, with curiosity and consistency.

- I hope it can also be helpful for other BAs or professionals who are exploring a similar path.
>>>>>>> d7927d3 (Update README with project overview and usage instructions)
