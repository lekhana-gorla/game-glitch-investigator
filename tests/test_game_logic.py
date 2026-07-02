from game import calculate_score, give_hint, is_valid_guess


def test_calculate_score_correct():
    assert calculate_score(0, 5, 5) == 10


def test_calculate_score_wrong():
    assert calculate_score(10, 3, 5) == 8


def test_hint_greater_than_five():
    assert give_hint(8) == "The number is greater than 5."


def test_hint_five_or_less():
    assert give_hint(4) == "The number is 5 or less."


def test_valid_guess():
    assert is_valid_guess(5) is True


def test_invalid_guess_low():
    assert is_valid_guess(0) is False


def test_invalid_guess_high():
    assert is_valid_guess(15) is False