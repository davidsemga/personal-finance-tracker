# Personal Finance Tracker

A simple **Python-based personal finance tracker** that lets you log spending, categorize expenses, and visualize monthly summaries with graphs. Built with **pandas** and **matplotlib**.

---

## Features

- Log spending with:
  - Date
  - Category (Food, Transport, Bills, Entertainment, Other)
  - Description
  - Amount
- View **monthly spending summaries** in tabular format.
- **Stacked bar charts** showing spending by category for each month.
- Data is stored in a CSV file (`spending.csv`) for persistence.

---

## Installation

1. Make sure you have **Python 3** installed.  
2. Install required packages:

```bash
pip3 install pandas matplotlib

```
3. Download or clone this repository.

## Usage

Run the script from your terminal:

``` bash
python3 finance_tracker.py

```

Menu options:

Log Spending – Enter new expenses.

View Monthly Summary – See tables and bar graphs of your spending.

Exit – Close the tracker.


## License

This project is open source and free to use :)

```yaml
✅ IF YOU WANT: Add a `.gitignore` file so your CSV doesn’t get uploaded:
```
spending.csv


Then commit both:

```bash
git add README.md .gitignore
git commit -m "Add README and gitignore"
git push
```
