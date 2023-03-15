from logic_functions import calculate_winner, get_fresh_board, get_next_board


def test_get_fresh_board():
    actual = get_fresh_board()
    expected = [None, None, None, None, None, None, None, None, None]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_calculate_winner_X():
    actual = calculate_winner(["X", None, None, None, "X", None, None, None, "X", None])
    expected = "X"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_calculate_winner_O():
    actual = calculate_winner(["X", None, None, None, "X", None, "O", "O", "O", "X"])
    expected = "O"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_get_next_board():
    actual = get_next_board(
        ["X", None, None, None, None, None, None, None, None], 3, False
    )
    expected = ["X", None, None, "O", None, None, None, None, None]

    assert actual == expected, f"Returned {actual} instead of {expected}"
