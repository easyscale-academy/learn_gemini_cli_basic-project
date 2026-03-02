# -*- coding: utf-8 -*-
"""
Tests for the Expense Analyzer implementation.

Run with: mise run test

These tests verify that your implementation correctly:
1. Returns a dictionary from main()
2. Contains all 6 expense categories
3. Has the correct maximum expense for each category in Q3 2025
"""

from expense_analyzer.impl import main


def test_main_returns_dict():
    """main() should return a dictionary."""
    result = main()
    assert isinstance(result, dict), f"Expected dict, got {type(result)}"


def test_main_has_all_categories():
    """The result should contain all 6 expense categories."""
    result = main()
    expected_categories = {
        "Dining",
        "Entertainment",
        "Groceries",
        "Shopping",
        "Transport",
        "Utilities",
    }
    assert set(result.keys()) == expected_categories, (
        f"Expected categories {expected_categories}, got {set(result.keys())}"
    )


def test_main_correct_max_expenses():
    """The result should have the correct max expense for each Q3 2025 category."""
    result = main()
    expected = {
        "Dining": 320.0,
        "Entertainment": 199.0,
        "Groceries": 198.5,
        "Shopping": 156.0,
        "Transport": 52.4,
        "Utilities": 145.8,
    }
    for category, expected_amount in expected.items():
        assert category in result, f"Missing category: {category}"
        assert result[category] == expected_amount, (
            f"{category}: expected {expected_amount}, got {result[category]}"
        )
