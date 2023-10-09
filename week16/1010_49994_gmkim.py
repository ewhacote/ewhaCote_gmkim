"""
Programmers 49994 방문 길이
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/49994
"""

import sys
input = sys.stdin.readline

def solution(dirs):
    answer = set()
    x, y = 0, 0
    opr = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    for d in dirs:
        nx, ny = x + opr[d][0], y + opr[d][1]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add(((x, y), (nx, ny)))
            answer.add(((nx, ny), (x, y)))

            x, y = nx, ny

    return len(answer) // 2

if __name__ == "__main__":

    dirs = str(input())

    print(solution(dirs))