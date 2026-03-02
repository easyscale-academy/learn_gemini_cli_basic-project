# -*- coding: utf-8 -*-
"""
Expense Analyzer — Student Implementation

Implement the functions below to analyze expense data from a TSV file.
Each function has a TODO comment explaining what to do.

Tech stack:
- Polars: A fast DataFrame library (like pandas but faster)
- Polars SQL: Query DataFrames using SQL syntax
- pytest: Testing framework

Run tests with: mise run test
"""

import polars as pl
from pathlib import Path


def get_data_path() -> Path:
    """Return the path to expense.tsv relative to this file."""
    return Path(__file__).parent.parent / "expense.tsv"


def load_expense_data() -> pl.DataFrame:
    """
    Load expense data from the TSV file into a Polars DataFrame.

    TODO: Implement this function
    - Use pl.read_csv() to read the TSV file
    - The file uses tab (\t) as separator
    - Use get_data_path() to get the file path

    Returns:
        pl.DataFrame: The loaded expense data
    """
    pass


def preview_first_rows(df: pl.DataFrame, n: int = 5) -> pl.DataFrame:
    """
    Preview the first N rows of the DataFrame using SQL.

    TODO: Implement this function
    - Create a Polars SQLContext and register the DataFrame
    - Use SQL to SELECT the first N rows (LIMIT)
    - Return the result as a DataFrame

    Args:
        df: The expense DataFrame
        n: Number of rows to preview (default: 5)

    Returns:
        pl.DataFrame: First N rows
    """
    pass


def filter_q3_data(df: pl.DataFrame) -> pl.DataFrame:
    """
    Filter the DataFrame to only include Q3 2025 transactions (July-September).

    TODO: Implement this function
    - Create a Polars SQLContext and register the DataFrame
    - Use SQL WHERE clause to filter dates between 2025-07-01 and 2025-09-30
    - Return the filtered DataFrame

    Args:
        df: The expense DataFrame

    Returns:
        pl.DataFrame: Only Q3 2025 transactions
    """
    pass


def find_max_expense_per_category(df: pl.DataFrame) -> dict:
    """
    Find the maximum expense amount for each category in Q3 2025.

    TODO: Implement this function
    - First filter to Q3 2025 data (you can reuse filter_q3_data)
    - Create a Polars SQLContext and register the Q3 DataFrame
    - Use SQL GROUP BY category and MAX(amount)
    - Convert the result to a dictionary {category: max_amount}

    Args:
        df: The expense DataFrame

    Returns:
        dict: {category_name: max_amount} for Q3 2025
    """
    pass


def main():
    """
    Main function that orchestrates the analysis.
    This is what the tests call.
    """
    # Step 1: Load the data
    df = load_expense_data()
    if df is None:
        print("ERROR: load_expense_data() returned None. Implement it first!")
        return None

    # Step 2: Preview the data (optional, for your understanding)
    print("=== First 5 rows ===")
    preview = preview_first_rows(df, 5)
    if preview is not None:
        print(preview)
    else:
        print("preview_first_rows() not implemented yet")

    # Step 3: Filter to Q3
    print("\n=== Q3 2025 Data ===")
    q3_data = filter_q3_data(df)
    if q3_data is not None:
        print(f"Q3 transactions: {len(q3_data)} rows")
    else:
        print("filter_q3_data() not implemented yet")

    # Step 4: Find max per category
    print("\n=== Max Expense Per Category (Q3 2025) ===")
    result = find_max_expense_per_category(df)
    if result is not None:
        for category, amount in sorted(result.items()):
            print(f"  {category}: ${amount:.2f}")
    else:
        print("find_max_expense_per_category() not implemented yet")

    return result


if __name__ == "__main__":
    main()
