
from hypothesis import given, strategies as st
from loan_eligibility import parse_income, monthly_emi, pan_category
import math


# --------------------------------
# 1. FUZZ TESTING PARSE_INCOME
# --------------------------------

@given(st.text() | st.none())
def test_parse_income_no_crash(s):
    try:
        result = parse_income(s)

        assert isinstance(result, int)
        assert result >= 0

    except ValueError:
        pass


# --------------------------------
# 2. FUZZ TESTING MONTHLY_EMI
# --------------------------------

@given(st.text() | st.none())
def test_monthly_emi_no_crash(s):
    try:
        result = monthly_emi(s)

        assert isinstance(result, (int, float))
        assert math.isfinite(result)
        assert result >= 0

    except ValueError:
        pass


# --------------------------------
# 3. FUZZ TESTING PAN_CATEGORY
# --------------------------------

@given(st.text() | st.none())
def test_pan_category_no_crash(s):
    try:
        result = pan_category(s)

        assert result in [
            "Individual",
            "Company",
            "HUF",
            "Firm"
        ]

    except ValueError:
        pass


# --------------------------------
# 4. ADDITIONAL VALID INPUT TESTS
# --------------------------------

def test_valid_income():
    assert parse_income("50,000") == 50000


def test_valid_emi():
    result = monthly_emi("500000,10,5")
    assert result > 0


def test_zero_interest_emi():
    assert monthly_emi("120000,0,1") == 10000


def test_valid_pan():
    assert pan_category("ABCPE1234F") == "Individual"
