"""
Programmers 169199 리코쳇 로봇
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/169199
"""

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(i, j, row, col, board):
    visited = [[0] * col for _ in range(row)]
    queue = deque()

    visited[i][j] = 1
    queue.append((i, j))

    while queue:
        a, b = queue.popleft()

        if board[a][b] == 'G':
            return visited[a][b] - 1

        for i in range(4):
            nx, ny = a, b

            while True:
                nx, ny = nx + dx[i], ny + dy[i]
                if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                if nx < 0 or nx >= row or ny < 0 or ny >= col:
                    nx -= dx[i]
                    ny -= dy[i]
                    break

            if not visited[nx][ny]:
                visited[nx][ny] = visited[a][b] + 1
                queue.append((nx, ny))

    return -1

def solution(board):

    row = len(board)
    col = len(board[0])

    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                return BFS(i, j, row, col, board)


if __name__ == "__main__":

    board = list(map(str, input().split()))

    print(solution(board))