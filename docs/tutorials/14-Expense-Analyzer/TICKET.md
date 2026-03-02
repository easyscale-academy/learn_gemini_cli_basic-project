# Learn Gemini CLI Basic 14 - Expense Analyzer: Complete the AI-Assisted Development Exercise

## Objective

Build a Python expense analyzer that finds the highest spending in each category from Q3 2025 transaction data.

Read the tutorial: [Expense Analyzer Exercise](https://github.com/easyscale-academy/learn_gemini_cli_basic-project/tree/14-Expense-Analyzer/)

The goal is not just to make tests pass—it's to practice **AI-assisted development skills**: describing tasks clearly, asking for explanations, iterating with tests, and applying divide-and-conquer thinking.

## Actionable Items

1. **Set up your environment** — Run `mise run venv-create` and `mise run inst`

2. **Implement the four core functions in `expense_analyzer/impl.py`:**
   - `load_expense_data()` — Read TSV file into Polars DataFrame
   - `preview_first_rows()` — Use SQL to display first N rows
   - `filter_q3_data()` — Filter to Q3 2025 using SQL
   - `find_max_expense_per_category()` — Find max expense per category using SQL

3. **Test your work** — Run `mise run test` after each function

4. **Verify all tests pass** — All 3 tests should pass

## Checklist

- [ ] **Environment set up** — Virtual environment created and dependencies installed
- [ ] **`load_expense_data()` implemented** — Reads TSV file
- [ ] **`preview_first_rows()` implemented** — Uses SQL to select first N rows
- [ ] **`filter_q3_data()` implemented** — Filters to Q3 2025
- [ ] **`find_max_expense_per_category()` implemented** — Finds max per category
- [ ] **All tests pass** — `mise run test` shows 3 passing tests
- [ ] **Learning complete** — You understand each function and can explain your AI collaboration method

## Submission & Verification

Run `/teach-check` to verify. Say "ship it" when complete to generate RESULT.md.
