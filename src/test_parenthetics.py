"""Test proper_parenthetics for proper output."""

from parenthetics import proper_parenthetics


def test_parenthetics_with_open_condition_single_entry():
    """Test that open parenthetics returns 1."""
    assert proper_parenthetics("(") == 1


def test_parenthetics_with_broken_condition():
    """Test that broken parenthetics returns -1."""
    assert proper_parenthetics(")(()))") == -1


def test_parenthetics_with_open_condition():
    """Test that broken parenthetics returns 1."""
    assert proper_parenthetics("()()())((") == 1


def test_parenthetics_with_balanced_condition():
    """Test that balanced parenthectics returns 0."""
    assert proper_parenthetics("(())((()())())") == 0
