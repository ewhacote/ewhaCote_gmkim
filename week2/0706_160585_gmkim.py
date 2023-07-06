"""
Programmers 160585 혼자서 하는 틱택토
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/160585
"""

import sys
input = sys.stdin.readline


def solution(board):

    O_cnt = X_cnt = 0

    # Error Case 1 - "O"를 표시할 차례인데 "X"를 표시하거나 반대로 "X"를 표시할 차례인데 "O"를 표시한다
    total = ''.join(board)
    valid = total.count('O') - total.count('X')
    if valid not in [0, 1]:
        return 0

    # Error Case 2 - 선공이나 후공이 승리해서 게임이 종료되었음에도 그 게임을 진행한다.
    board_col = list(zip(board))
    for i in range(3):
        if board[i].count('O') == 3 or board_col[i].count('O') == 3:
            O_cnt += 1
        elif board[i].count('X') == 3 or board_col[i].count('X') == 3:
            X_cnt += 1

    for i in range(0, 3, 2):
        if board[0][i] == board[1][1] == board[2][2-i] == 'O':
            O_cnt += 1
        elif board[0][i] == board[1][1] == board[2][2-i] == 'X':
            X_cnt += 1

    if O_cnt and X_cnt:
        return 0
    elif O_cnt == 1 and valid == 0:
        return 0
    elif X_cnt == 1 and valid >= 1:
        return 0

    return 1


if __name__ == "__main__":

    board = ["O.X", ".O.", "..X"]
    # baord = ["OOO", "...", "XXX"]
    # board = ["...", ".X.", "..."]
    # board = ["...", "...", "..."]

    print(solution(board))