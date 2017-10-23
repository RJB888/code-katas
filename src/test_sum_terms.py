"""Test series_sum function for proper output."""


def test_series_sum_1():
    """Verify that series_sum(1) == '1.00'."""
    from sum_of_nth_terms import series_sum
    assert series_sum(1) == "1.00"


def test_series_sum_2():
    """Verify that series_sum(2) == '1.25'."""
    from sum_of_nth_terms import series_sum
    assert series_sum(2) == "1.25"


def test_series_sum_3():
    """Verify that series_sum(3) == '1.39'."""
    from sum_of_nth_terms import series_sum
    assert series_sum(3) == "1.39"
