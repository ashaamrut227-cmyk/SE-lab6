
import pytest

from traffic_fine import (
    speeding_fine,
    license_action,
    total_penalty
)


# 1. SPEEDING FINE - BRANCH TESTS

def test_speed_within_limit():
    assert speeding_fine(50, 60, "city") == 0


def test_speed_equal_to_limit():
    assert speeding_fine(60, 60, "city") == 0


def test_school_zone():
    assert speeding_fine(70, 60, "school") == 2000


def test_highway_zone():
    assert speeding_fine(70, 60, "highway") == 1000


def test_other_zone():
    assert speeding_fine(70, 60, "city") == 500


def test_excess_above_40():
    assert speeding_fine(110, 60, "school") == 6000


def test_excess_equal_to_40():
    assert speeding_fine(100, 60, "school") == 4000


def test_excess_between_20_and_40():
    assert speeding_fine(90, 60, "highway") == 2000


def test_excess_equal_to_20():
    assert speeding_fine(80, 60, "city") == 500


# 2. LICENSE ACTION - BRANCH TESTS

def test_points_at_least_12_commercial():
    assert license_action(12, True, False) == "revoke"


def test_points_at_least_12_non_commercial():
    assert license_action(12, False, False) == "suspend"


def test_points_between_8_and_11_repeat():
    assert license_action(9, False, True) == "suspend"


def test_points_between_8_and_11_not_repeat():
    assert license_action(9, False, False) == "warning"


def test_points_between_4_and_7():
    assert license_action(5, False, False) == "notice"


def test_points_below_4():
    assert license_action(2, False, False) == "none"


# 3. TOTAL PENALTY - BRANCH TESTS

def test_normal_total():
    assert total_penalty([1000, 2000, 3000]) == 6000


def test_empty_fines_list():
    assert total_penalty([]) == 0


def test_negative_fine():
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([1000, -500])


def test_total_exceeds_10000():
    assert total_penalty([5000, 6000]) == 10000


def test_total_equal_to_10000():
    assert total_penalty([5000, 5000]) == 10000
