"""
Programmers 159993 미로 탈출
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/159993
"""

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(s, e, maps):

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    q = deque()
    flag = False

    for i in range(n):
        for j in range(m):
            if maps[i][j] == s:
                q.append((i, j, 0))
                visited[i][j] = True
                flag = True
                break
        if flag:
            break

    while q:
        y, x, cost = q.popleft()

        if maps[y][x] == e:
            return cost

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != 'X':
                if not visited[ny][nx]:
                    q.append((ny, nx, cost+1))
                    visited[ny][nx] = True
    return -1

def solution(maps):
    path1 = BFS('S', 'L', maps)
    path2 = BFS('L', 'E', maps)

    if path1 != -1 and path2 != -1:
        return path1 + path2

    return -1

if __name__ == "__main__":

    # maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
    maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]

    print(solution(maps))