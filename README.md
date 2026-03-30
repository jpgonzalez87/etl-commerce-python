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
