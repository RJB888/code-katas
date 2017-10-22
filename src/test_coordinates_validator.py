"""Test is_valid_coordinates to ensure valid output."""

import pytest

COORDINATE_LIST = [("-23, 25", True),
                   ("4, -3", True),
                   ("24.53525235, 23.45235", True),
                   ("04, -23.234235", True),
                   ("43.91343345, 143", True),
                   ("23.234, - 23.4234", False),
                   ("2342.43536, 34.324236", False),
                   ("N23.43345, E32.6457", False),
                   ("99.234, 12.324", False),
                   ("6.325624, 43.34345.345", False),
                   ("0, 1,2", False),
                   ("0.342q0832, 1.2324", False),
                   ("23.245, 1e1", False),
                   ("0, 0", True),
                   ("-10, 5", True),
                   ("N33, W22", False),
                   ("-200, -300", False)]


@pytest.mark.parametrize('coords, output', COORDINATE_LIST)
def test_is_valid_coordinates(coords, output):
    """Test for valid responses given coordinates."""
    from coordinates_validator import is_valid_coordinates
    assert is_valid_coordinates(coords) == output


# # Test.describe("Example Test Cases")

# # Test.it("should return true for valid coordinates")
# # valid_coordinates = [
# #     "-23, 25",
# #     "4, -3",
# #     "24.53525235, 23.45235",
# #     "04, -23.234235",
# #     "43.91343345, 143"
# # ]

# # for coordinate in valid_coordinates:
# #     test.expect(is_valid_coordinates(coordinate),
#  "%s validation failed." % coordinate)

# # Test.it("should return false for invalid coordinates")
# # invalid_coordinates = [
# #     "23.234, - 23.4234",
# #     "2342.43536, 34.324236",
# #     "N23.43345, E32.6457",
# #     "99.234, 12.324",
# #     "6.325624, 43.34345.345",
# #     "0, 1,2",
# #     "0.342q0832, 1.2324",
# #     "23.245, 1e1"
# # ]

# # for coordinate in invalid_coordinates:
# #     test.expect(not is_valid_coordinates(coordinate),
# "%s validation failed." % coordinate)
