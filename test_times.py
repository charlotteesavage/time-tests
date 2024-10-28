from times import time_range, compute_overlap_time
import pytest


@pytest.mark.parametrize(
    "large, short, expected",
    # normal range
    [
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
        [
            ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
            ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
        ],
    ],
    # two ranges that do not overlap
    [
        time_range("2024-01-12 10:00:00", "2024-01-12 12:00:00"),
        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
        [],
    ],
    # ranges with several intervals
    [
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3),
        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
        [
            ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
            ("2010-01-12 10:38:00", "2010-01-12 10:40:00"),
            ("2010-01-12 10:40:00", "2010-01-12 10:45:00"),
        ],
    ],
    # adjacent time intervals
    [
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00"),
        [],
    ],
)
def test_given_input(large, short, expected):
    result = compute_overlap_time(large, short)
    assert result == expected, f"Expected: {expected}, Actual: {result}"


def test_backwards_time_range():
    expected_error_message = "Start time is after end time!"
    with pytest.raises(ValueError, match=expected_error_message):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
