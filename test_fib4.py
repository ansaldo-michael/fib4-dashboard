from fib4 import calculate_fib4

def test_example():
    # (50 × 40) ÷ (200 × √25) = 2000 ÷ 1000 = 2.0
    assert calculate_fib4(50, 40, 25, 200) == 2.0

def test_low_score():
    # (40 × 20) ÷ (250 × √25) = 800 ÷ 1250 = 0.64
    assert round(calculate_fib4(40, 20, 25, 250), 2) == 0.64

def test_high_score():
    # (65 × 60) ÷ (150 × √36) = 3900 ÷ 900 = 4.33
    assert round(calculate_fib4(65, 60, 36, 150), 2) == 4.33

def test_non_square_alt():
    # (50 × 40) ÷ (200 × √30) = 2000 ÷ 1095.4 = 1.83
    assert round(calculate_fib4(50, 40, 30, 200), 2) == 1.83

import pytest

def test_platelets_zero_rejected():
    with pytest.raises(ValueError):
        calculate_fib4(50, 40, 25, 0)

def test_alt_too_high_rejected():
    with pytest.raises(ValueError):
        calculate_fib4(50, 40, 10001, 200)

def test_platelets_too_high_rejected():
    with pytest.raises(ValueError):
        calculate_fib4(50, 40, 25, 200000)

def test_age_too_young_rejected():
    with pytest.raises(ValueError):
        calculate_fib4(17, 40, 25, 200)

def test_text_input_rejected():
    with pytest.raises(ValueError):
        calculate_fib4(50, "abc", 25, 200)

from fib4 import classify_fib4, get_warnings

def test_low_below_cutoff_under_65():
    assert classify_fib4(1.2, 50) == "Low"

def test_exactly_1_3_is_indeterminate_under_65():
    assert classify_fib4(1.3, 50) == "Indeterminate"

def test_1_3_is_low_over_65():
    assert classify_fib4(1.3, 70) == "Low"

def test_exactly_2_0_is_indeterminate_over_65():
    assert classify_fib4(2.0, 70) == "Indeterminate"

def test_high_cutoff():
    assert classify_fib4(2.67, 50) == "Indeterminate"
    assert classify_fib4(2.68, 50) == "High"

def test_age_65_uses_older_table():
    assert classify_fib4(1.8, 65) == "Low"
    assert classify_fib4(1.8, 64) == "Indeterminate"

def test_no_warnings_normal_case():
    assert get_warnings(50, 40, 25) == []

def test_age_warnings():
    assert len(get_warnings(34, 40, 25)) == 1
    assert get_warnings(35, 40, 25) == []
    assert get_warnings(64, 40, 25) == []
    assert len(get_warnings(65, 40, 25)) == 1

def test_enzyme_warnings():
    assert get_warnings(50, 300, 25) == []
    assert len(get_warnings(50, 301, 25)) == 1
    assert len(get_warnings(50, 40, 301)) == 1
