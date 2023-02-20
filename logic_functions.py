def calculate_winner(squares):
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for a, b, c in lines:
        if squares[a] == squares[b] and squares[a] == squares[c]:
            return squares[a]
    return None


def get_fresh_board():
   return [None for _ in range(9)]



def get_next_board(squares, i, x_is_next):
    if squares[i] == "X":
        x_is_next = "O"
    else:
        x_is_next = "X"
    return x_is_next