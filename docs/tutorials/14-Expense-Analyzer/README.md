# Expense Analyzer

> Practice AI-assisted development by building a Python expense analyzer — intentionally using an unfamiliar tech stack.

## Overview

This exercise is different from previous lessons. Instead of learning a specific Gemini CLI feature, you'll practice using Gemini CLI as a development partner to build something real with tools you may not know yet.

You'll work with **Python**, **Polars** (a fast DataFrame library), and **SQL queries** to analyze expense data. The goal isn't to master Python or Polars — it's to practice a transferable skill: **collaborating with AI to work through unfamiliar territory**.

## What You'll Build

A Python function that:
1. Reads a TSV file of expense transactions
2. Filters to Q3 2025 (July-September) transactions
3. Finds the highest spending in each category
4. Returns the results as a dictionary

## Learning Objectives

1. **Describing tasks clearly** — Breaking down what you want into specific requests
2. **Asking for explanations** — Understanding *why* code works, not just accepting it
3. **Test-driven iteration** — Using failing tests to guide implementation
4. **Divide-and-conquer thinking** — Solving small pieces individually

## Exercises

1. Set up the development environment
2. Implement `load_expense_data()` — Read the TSV file
3. Implement `preview_first_rows()` — SQL SELECT with LIMIT
4. Implement `filter_q3_data()` — SQL WHERE for Q3 dates
5. Implement `find_max_expense_per_category()` — SQL GROUP BY with MAX
6. Run all tests and verify

## Getting Started

Switch to the branch and read the full tutorial:

```bash
git checkout 14-Expense-Analyzer
```

Then open `README.md` for the complete walkthrough.
