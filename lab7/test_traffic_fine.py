
from hypothesis import given, strategies as st
from traffic_fine import parse_ticket_id, total_fines, speed_excess


# Fuzz testing for parse_ticket_id()
@given(st.one_of(st.text(), st.none()))
def test_parse_ticket_id_no_crash(s):
    parse_ticket_id(s)


# Fuzz testing for total_fines()
@given(st.one_of(st.text(), st.none()))
def test_total_fines_no_crash(s):
    total_fines(s)


# Fuzz testing for speed_excess()
@given(st.one_of(st.text(), st.none()))
def test_speed_excess_no_crash(s):
    speed_excess(s)
