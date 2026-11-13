
import pytest

from traffic_fine import (
    speeding_fine,
    license_action,
    total_penalty
)


# ==========================================
# 1. SPEEDING FINE TEST CASES
# ==========================================

def test_speed_not_exceeding_limit():
    assert speeding_fine(50, 60, "city") == 0


def test_school_zone_fine():
    assert speeding_fine(70, 60, "school") == 2000


def test_highway_zone_fine():
    assert speeding_fine(70, 60, "highway") == 1000


def test_other_zone_fine():
    assert speeding_fine(70, 60, "city") == 500


def test_excess_speed_above_40():
    assert speeding_fine(110, 60, "school") == 6000


def test_excess_speed_between_20_and_40():
    assert speeding_fine(90, 60, "highway") == 2000


def test_excess_speed_equal_to_20():
    assert speeding_fine(80, 60, "city") == 500


# ==========================================
# 2. LICENSE ACTION TEST CASES
# ==========================================

def test_commercial_driver_revoke():
    assert license_action(12, True, False) == "revoke"


def test_non_commercial_driver_suspend():
    assert license_action(12, False, False) == "suspend"


def test_repeat_offender_suspend():
    assert license_action(9, False, True) == "suspend"


def test_non_repeat_offender_warning():
    assert license_action(9, False, False) == "warning"


def test_license_notice():
    assert license_action(5, False, False) == "notice"


def test_license_no_action():
    assert license_action(2, False, False) == "none"


# ==========================================
# 3. TOTAL PENALTY TEST CASES
# ==========================================

def test_total_penalty_normal():
    assert total_penalty([1000, 2000, 3000]) == 6000


def test_total_penalty_empty_list():
    assert total_penalty([]) == 0


def test_total_penalty_exceeds_limit():
    assert total_penalty([5000, 6000]) == 10000


def test_negative_fine_raises_error():
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([1000, -500])
