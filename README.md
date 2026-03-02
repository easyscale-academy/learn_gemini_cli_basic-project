# Expense Analyzer

> Practice AI-assisted development by building a Python expense analyzer — intentionally using an unfamiliar tech stack.

## Overview

This exercise is different from previous lessons. Instead of learning a specific Gemini CLI feature, you'll practice using Gemini CLI as a development partner to build something real with tools you may not know yet.

You'll work with **Python**, **Polars** (a fast DataFrame library), and **SQL queries** to analyze expense data. If these are unfamiliar — that's the point. The goal isn't to master Python or Polars. It's to practice a transferable skill: **collaborating with AI to work through unfamiliar territory**.

This is what real-world AI-assisted development looks like. You describe what you want, the AI helps you build it, and you learn by asking questions along the way.

## Learning Objectives

By the end of this exercise, you'll have practiced:

1. **Describing tasks clearly** — Breaking down what you want into specific, actionable requests
2. **Asking for explanations** — Not just accepting code, but understanding *why* it works
3. **Test-driven iteration** — Using failing tests to guide your implementation, one function at a time
4. **Divide-and-conquer thinking** — Tackling a complex problem by solving small pieces individually

## Prerequisites

Before starting this exercise, you should have:

- **Command line basics** — You can navigate directories and run commands
- **An AI assistant** (Gemini CLI, Cursor, etc.) — Installed and working
- **Willingness to experiment** — You don't need Python experience; the AI will help

> **Note:** You do NOT need to know Python, Polars, or SQL beforehand. Learning to work with unfamiliar tools through AI assistance is exactly the skill we're practicing.

---

## What You'll Build

A Python function that:
1. Reads a TSV (tab-separated) file of expense transactions
2. Filters to Q3 2025 (July–September) transactions only
3. Finds the highest spending in each category
4. Returns the results as a dictionary

**Example output:**
```python
{
    'Dining': 320.0,
    'Entertainment': 199.0,
    'Groceries': 198.5,
    'Shopping': 156.0,
    'Transport': 52.4,
    'Utilities': 145.8
}
```

---

## Key Concepts

Before diving in, here's a brief overview of the tools you'll encounter. Don't worry about memorizing these — you'll learn them hands-on, and you can always ask Gemini to explain.

### Python Project Structure

```
expense_analyzer/
├── __init__.py          # Makes this a Python package
├── impl.py              # Your implementation (where you write code)
├── impl_example.py      # Reference implementation (don't peek yet!)
├── expense.tsv          # The data file (119 transactions)
├── tests/
│   └── test_impl.py     # Tests that verify your code works
├── pyproject.toml       # Project configuration and dependencies
└── mise.toml            # Task runner configuration
```

### uv — Python Package Manager

**uv** is a fast Python package manager (think npm for Python). We use it through mise:

- `mise run venv-create` — Creates an isolated Python environment
- `mise run inst` — Installs dependencies listed in `pyproject.toml`

### Polars — Data Processing Library

**Polars** is a fast DataFrame library for Python. Think of it as a super-powered spreadsheet in code:

```python
import polars as pl

# Read a file into a DataFrame
df = pl.read_csv("data.tsv", separator="\t")

# Access columns, filter rows, aggregate data
```

### SQL Interface

Polars lets you query DataFrames using SQL — a language designed for data questions:

```python
# Register a DataFrame for SQL queries
ctx = pl.SQLContext({"expenses": df})

# Ask questions in SQL
result = ctx.execute("SELECT * FROM expenses WHERE amount > 100").collect()
```

### pytest — Testing Framework

**pytest** runs your tests and tells you what's working:

```bash
mise run test
```

Green = passing. Red = failing with helpful error messages.

### Divide & Conquer

Instead of building everything at once, you'll implement one function at a time:

1. `load_expense_data()` — Just read the file
2. `preview_first_rows()` — Just show some rows
3. `filter_q3_data()` — Just filter by date
4. `find_max_expense_per_category()` — Just find the maximums

Each builds on the previous one. Each can be tested independently.

---

## Exercises

### Exercise 1: Set Up Your Environment

**Goal:** Get the project ready to run.

**What to do:**

Ask Gemini to help you set up:

```
Look at mise.toml and pyproject.toml. Help me set up the development environment for this project.
```

**What should happen:**
1. Run `mise run venv-create` to create a Python virtual environment
2. Look at `pyproject.toml` — notice the Polars dependency is commented out
3. Uncomment the Polars dependency line
4. Run `mise run inst` to install dependencies

**Verify it worked:**
```bash
mise run test
```

You should see test failures — that's expected! The functions aren't implemented yet. But if the tests *run* (even if they fail), your environment is set up correctly.

> **Key insight:** Setting up environments is a common stumbling block. AI assistants are great at reading config files and walking you through setup steps. Don't struggle alone — describe what you see and ask for help.

---

### Exercise 2: Implement `load_expense_data()`

**Goal:** Read the TSV file into a Polars DataFrame.

**Open `expense_analyzer/impl.py`** and find the `load_expense_data()` function. It has a TODO comment explaining what to do.

**Ask Gemini for help:**

```
Look at expense_analyzer/impl.py. Help me implement the load_expense_data() function.
I need to read expense.tsv (tab-separated) into a Polars DataFrame.
```

**After implementing, ask Gemini to explain:**

```
/teach-explain How does pl.read_csv() work with TSV files? Why do we need separator="\t"?
```

> **Key insight:** Don't just accept the code. Ask "why" and "how" — understanding the approach is more valuable than the specific syntax.

---

### Exercise 3: Implement `preview_first_rows()`

**Goal:** Use SQL to select the first N rows from the DataFrame.

**Ask Gemini:**

```
Help me implement preview_first_rows() in impl.py.
It should use Polars SQL to select the first N rows. Look at the TODO for details.
```

**Key concept to explore:**

```
/teach-explain What is a SQL context in Polars? Why register a DataFrame before querying?
```

> **Key insight:** SQL is a powerful language for data questions. Even if you've never used it, the syntax reads almost like English: `SELECT * FROM expenses LIMIT 5`.

---

### Exercise 4: Implement `filter_q3_data()`

**Goal:** Filter transactions to Q3 2025 only (July 1 – September 30).

**Ask Gemini:**

```
Help me implement filter_q3_data() in impl.py.
I need to filter to Q3 2025 (July-September) using SQL WHERE clause on the date column.
```

**Test your progress:**
```bash
mise run test
```

You should start seeing some tests pass!

> **Key insight:** Date filtering is a common real-world task. SQL makes it readable: `WHERE date >= '2025-07-01' AND date <= '2025-09-30'`.

---

### Exercise 5: Implement `find_max_expense_per_category()`

**Goal:** Find the highest spending in each category using SQL GROUP BY.

**Ask Gemini:**

```
Help me implement find_max_expense_per_category() in impl.py.
I need to GROUP BY category and find MAX(amount) for Q3 2025 data, then return it as a dictionary.
```

**Explore the SQL concepts:**

```
/teach-explain What does GROUP BY do in SQL? How does MAX() work with it?
```

> **Key insight:** GROUP BY + aggregate functions (MAX, SUM, AVG) are the foundation of data analysis. Understanding this pattern unlocks a huge range of real-world data questions.

---

### Exercise 6: Run All Tests

**Goal:** Verify everything works together.

```bash
mise run test
```

**Expected result:** 3 tests passing.

If tests fail, use Gemini to debug:

```
/teach-debug Here's my test output: [paste the error]. Help me figure out what's wrong.
```

**When all tests pass**, run:
```
/teach-check
```

---

## Reflection

After completing the exercises, consider these questions:

1. **How did you describe tasks to Gemini?** Did your prompts get more specific as you went?
2. **What did you learn by asking "why"?** Which explanations surprised you?
3. **How did failing tests help?** Did the error messages guide your next steps?
4. **Could you apply this method to another unfamiliar stack?** (e.g., Rust, Go, a new framework)

The method you practiced — describe, implement, test, ask why — works with any technology. That's the real skill here.

---

## Mentor's Note

**Why this exercise matters:**

I've seen experienced developers freeze when they encounter an unfamiliar stack. "I don't know Python" becomes a wall they can't get past.

But here's the thing: **you don't need to know everything upfront anymore**. AI assistants change the equation. The skill that matters is knowing how to *collaborate* — how to describe what you want, how to ask the right questions, how to verify the answer is correct.

This exercise is intentionally outside your comfort zone. The Python, Polars, and SQL are just the vehicle. What you're really practicing is:

- **Breaking problems into pieces** — Not "build an expense analyzer" but "read this file, filter these rows, group by this column"
- **Communicating clearly** — Vague prompts get vague answers. Specific prompts get working code.
- **Learning through testing** — Tests tell you if you're on track before you fully understand the code.
- **Building understanding incrementally** — You don't need to understand everything at once. Each function teaches you a bit more.

These skills transfer to any technology, any project, any team. That's why this exercise exists.

---

## Quick Reference

**Environment setup:**
```bash
mise run venv-create    # Create virtual environment
mise run inst           # Install dependencies
```

**Run tests:**
```bash
mise run test           # Run all tests
```

**Teaching commands:**
```
/teach-start            # Start a guided learning session
/teach-code             # Get code help + learning notes
/teach-explain          # Understand a concept or code
/teach-debug            # Debug an error with guidance
/teach-check            # Verify your work
/teach-brainstorm       # Clarify an idea
```

**Key files:**
- `expense_analyzer/impl.py` — Your implementation
- `expense_analyzer/impl_example.py` — Reference (try not to peek!)
- `expense.tsv` — The data
- `tests/test_impl.py` — Tests

---

## Reference Implementation

A complete working implementation is provided in `expense_analyzer/impl_example.py`.

**Our recommendation:** Try to implement each function with AI assistance first. Only look at the reference if you're truly stuck and the AI explanations aren't helping. The learning happens in the struggle and the conversation, not in copying the answer.
