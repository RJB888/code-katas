"""Test grouped_by_commas produces proper result."""

import pytest

COMMA_GROUP_LIST = [(1, '1'),
                    (10, '10'),
                    (100, '100'),
                    (1000, '1,000'),
                    (10000, '10,000'),
                    (100000, '100,000'),
                    (1000000, '1,000,000'),
                    (35235235, '35,235,235'),
                    (12123, '12,123'),
                    (15, '15'),
                    (2345678, '2,345,678'),
                    (12345678900, '12,345,678,900')]


@pytest.mark.parametrize('n, res', COMMA_GROUP_LIST)
def test_grouped_by_commas(n, res):
    """Test input to verify output is as expected."""
    from grouped_by_commas import group_by_commas
    assert group_by_commas(n) == res
