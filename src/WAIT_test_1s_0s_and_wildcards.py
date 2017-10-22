"""Test 0s and 1s with wildcards."""
# from functools import reduce
import pytest

WILDCARD_LIST = [('101?', ['1010', '1011']),
                 ('10??', ['1000', '1001', '1010', '1011']),
                 ('1?1?', ['1010', '1011', '1110', '1111']),
                 ('1??', ['100', '101', '110', '111']),
                 ('10??1?', ['100010', '100011', '101010', '101110',
                  '101111']),
                 ('?1?', ['010', '011', '110', '111']),
                 ('11??0', ['11000', '11010', '11100', '11110'])]


# test.describe("basic tests")

# t1 = possibilities('101?')
# t1.sort()
# test.assert_equals(t1, ['1010', '1011'])

# t2 = possibilities('10??')
# t2.sort()
# test.assert_equals(t2, ['1000', '1001', '1010', '1011'])

# t3 = possibilities('1?1?')
# t3.sort()
# test.assert_equals(t3, ['1010', '1011', '1110', '1111'])

@pytest.mark.parametrize("input_string, result", WILDCARD_LIST)
def test_1s_and_0s_wildcards(input_string, result):
    """Pass values to function and see if they are valid."""
    from _1s_0s_and_wildcards import possibilities
    t1 = possibilities(input_string)
    t1.sort()
    assert t1 == result
