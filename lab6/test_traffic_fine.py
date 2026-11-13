
import pytest
from traffic_fine import speeding_fine, license_action, total_penalty


# 1. Tests for speeding_fine()

def test_no_speeding():
    assert speeding_fine(50, 60, "city") == 0

def test_school_zone():
    assert speeding_fine(70, 60, "school") == 2000

def test_highway_zone():
    assert speeding_fine(70, 60, "highway") == 1000

def test_city_zone():
    assert speeding_fine(70, 60, "city") == 500

def test_excess_speed_above_40():
    assert speeding_fine(105, 60, "city") == 1500

def test_excess_speed_above_20():
    assert speeding_fine(85, 60, "city") == 1000

def test_excess_speed_20_or_less():
    assert speeding_fine(75, 60, "city") == 500


# 2. Tests for license_action()

def test_clean_record():
    assert license_action(2, False, False) == "none"

def test_points_below_4():
    assert license_action(3, False, False) == "none"

def test_points_equal_4():
    assert license_action(4, False, False) == "notice"

def test_points_below_8():
    assert license_action(7, False, False) == "notice"

def test_points_equal_8():
    assert license_action(8, False, False) == "warning"

def test_repeat_offender():
    assert license_action(8, False, True) == "suspend"

def test_points_below_12():
    assert license_action(11, False, False) == "warning"

def test_points_equal_12():
    assert license_action(12, False, False) == "suspend"

def test_commercial_driver():
    assert license_action(12, True, False) == "revoke"


# 3. Tests for total_penalty()

def test_total_penalty_normal():
    assert total_penalty([100, 200, 300]) == 600

def test_total_penalty_empty_list():
    assert total_penalty([]) == 0

def test_total_penalty_single_fine():
    assert total_penalty([500]) == 500

def test_total_penalty_negative_fine():
    with pytest.raises(ValueError):
        total_penalty([100, -50, 200])

def test_total_penalty_above_limit():
    assert total_penalty([6000, 5000]) == 10000

def test_total_penalty_equal_to_limit():
    assert total_penalty([5000, 5000]) == 10000
