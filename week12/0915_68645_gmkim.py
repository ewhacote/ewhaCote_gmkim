"""
Programmers 68645 삼각 달팽이
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/68645
"""

import sys
input = sys.stdin.readline

def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    x, y, num = -1, 0, 1

    for i in range(n):
        for j in range(i, n):
            x, y = (x+1, y) if i%3==0 else (x, y+1) if i%3==1 else (x-1, y-1)
            answer[x][y] = num
            num += 1

    return sum(answer, [])

if __name__ == "__main__":

    n = int(input())

    print(solution(n))