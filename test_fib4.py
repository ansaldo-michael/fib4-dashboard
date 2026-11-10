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
