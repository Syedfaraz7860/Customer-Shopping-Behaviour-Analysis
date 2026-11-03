# 🛍️ Customer Shopping Behaviour Analysis

## 📌 Project Overview

**Customer Shopping Behaviour Analysis** is a Data Analytics project designed to analyze customer purchasing patterns and generate meaningful business insights from shopping data.

The project uses **Python, SQL, and Power BI** to perform data cleaning, data analysis, customer segmentation, and interactive data visualization.

The complete workflow is:

**Dataset → Python → SQL → Power BI Dashboard**

---

## 🎯 Project Objectives

* Analyze customer shopping behaviour
* Understand purchasing patterns
* Analyze revenue based on gender and product categories
* Identify customer segments
* Analyze the impact of discounts on purchases
* Find high-value customers
* Create an interactive Power BI dashboard
* Generate useful business insights from customer data

---

## 🛠️ Technologies Used

| Technology           | Purpose                         |
| -------------------- | ------------------------------- |
| 🐍 Python            | Data cleaning and preprocessing |
| 🐼 Pandas            | Data manipulation and analysis  |
| 🔢 NumPy             | Numerical operations            |
| 🗄️ PostgreSQL / SQL | Data analysis and querying      |
| 📊 Power BI          | Dashboard and visualization     |
| 💻 VS Code           | Development environment         |
| 🔗 Git & GitHub      | Version control                 |

---

## 📂 Project Structure

```text
Customer-Shopping-Behaviour-Analysis/
│
├── customer.py
├── customer_shopping_behavior.csv
├── customer_analysis.sql
├── PowerBI/
│   └── customer_shopping_analysis.pbix
│
├── screenshots/
│   └── dashboard.png
│
└── README.md
```

---

## 🐍 Python Data Analysis

Python was used for loading, cleaning, and preprocessing the dataset.

### Main tasks performed:

* Loaded the dataset using Pandas
* Checked dataset information
* Checked missing values
* Handled missing values
* Standardized column names
* Performed data transformation
* Created age groups
* Analyzed purchase frequency
* Prepared cleaned data for SQL analysis

Example:

```python
import pandas as pd
import numpy as np

df = pd.read_csv("customer_shopping_behavior.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
```

---

## 🗄️ SQL Analysis

SQL was used to perform business-related analysis on the cleaned customer data.

### Analysis included:

* Gender-wise revenue analysis
* Product/category analysis
* Discount-based purchase analysis
* Average purchase analysis
* Customer segmentation
* Purchase frequency analysis
* High-value customer identification
* Revenue aggregation
* Customer behaviour analysis

SQL concepts used:

```text
SELECT
WHERE
GROUP BY
ORDER
```
