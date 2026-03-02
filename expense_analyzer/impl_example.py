# -*- coding: utf-8 -*-
"""
Expense Analyzer — Reference Implementation

This is the complete working implementation.
Try to implement it yourself first before looking here!
"""

import polars as pl
from pathlib import Path


def get_data_path() -> Path:
    """Return the path to expense.tsv relative to this file."""
    return Path(__file__).parent.parent / "expense.tsv"


def load_expense_data() -> pl.DataFrame:
    """Load expense data from the TSV file into a Polars DataFrame."""
    return pl.read_csv(get_data_path(), separator="\t")


def preview_first_rows(df: pl.DataFrame, n: int = 5) -> pl.DataFrame:
    """Preview the first N rows using SQL."""
    ctx = pl.SQLContext({"expenses": df})
    return ctx.execute(f"SELECT * FROM expenses LIMIT {n}").collect()


def filter_q3_data(df: pl.DataFrame) -> pl.DataFrame:
    """Filter to Q3 2025 (July 1 - September 30)."""
    ctx = pl.SQLContext({"expenses": df})
    return ctx.execute(
        "SELECT * FROM expenses WHERE date >= '2025-07-01' AND date <= '2025-09-30'"
    ).collect()


def find_max_expense_per_category(df: pl.DataFrame) -> dict:
    """Find the maximum expense per category in Q3 2025."""
    q3_df = filter_q3_data(df)
    ctx = pl.SQLContext({"q3": q3_df})
    result = ctx.execute(
        "SELECT category, MAX(amount) as max_amount FROM q3 GROUP BY category"
    ).collect()

    return dict(zip(result["category"].to_list(), result["max_amount"].to_list()))


def main():
    """Main function that orchestrates the analysis."""
    df = load_expense_data()

    print("=== First 5 rows ===")
    print(preview_first_rows(df, 5))

    print("\n=== Q3 2025 Data ===")
    q3_data = filter_q3_data(df)
    print(f"Q3 transactions: {len(q3_data)} rows")

    print("\n=== Max Expense Per Category (Q3 2025) ===")
    result = find_max_expense_per_category(df)
    for category, amount in sorted(result.items()):
        print(f"  {category}: ${amount:.2f}")

    return result


if __name__ == "__main__":
    main()
