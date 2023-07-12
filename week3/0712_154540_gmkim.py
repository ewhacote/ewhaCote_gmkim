"""
Programmers 154540 무인도 여행
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154540
"""

import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    col, row = len(maps), len(maps[0])
    visited = [[False] * row for _ in range(col)]

    answer = []

    for i in range(col):
        for j in range(row):
            if maps[i][j] != "X" and not visited[i][j]:
                period = 0
                queue = [(j, i)]

                while queue:
                    x, y = queue.pop()
                    if visited[y][x]:
                        continue
                    visited[y][x] = True
                    period += int(maps[y][x])

                    for k in range(4):
                        ax, ay = x + dx[k], y + dy[k]
                        if -1 < ax < row and -1 < ay < col and maps[ay][ax] != "X" and not visited[ay][ax]:
                            queue.append((ax, ay))

                answer.append(period)

    return sorted(answer) if answer else [-1]

if __name__ == "__main__":

    maps = list(map(int, input().split()))

    print(solution(maps))