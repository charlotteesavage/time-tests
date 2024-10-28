from times import time_range, compute_overlap_time
import pytest


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
    ]
    assert result == expected, f"Expected: {expected}, Actual: {result}"


def test_two_ranges_do_not_overlap():
    large = time_range("2024-01-12 10:00:00", "2024-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected, f"Expected: {expected}, Actual: {result}"


def test_several_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:40:00"),
        ("2010-01-12 10:40:00", "2010-01-12 10:45:00"),
    ]
    assert result == expected, f"Expected: {expected}, Actual: {result}"


def test_different_starts_and_same_ends():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected, f"Expected: {expected}, Actual: {result}"


def test_backwards_time_range():
    expected_error_message = "Start time is after end time!"
    with pytest.raises(ValueError, match=expected_error_message):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
