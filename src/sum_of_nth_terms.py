"""Create a function to calculate a series."""
from __future__ import division


def series_sum(n):
    """Calculate total of series to the nth position."""
    print(n)
    if n < 2 >= 0:
        return '{:.2f}'.format(n)
    else:
        tot = 1
        for i in range(2, n + 1):
            denom = 0
            denom += (((i - 1) * 2) + i)
            tot += 1 / denom
    return '{:.2f}'.format(tot)
