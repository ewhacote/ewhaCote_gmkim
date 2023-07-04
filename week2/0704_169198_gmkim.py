"""
Programmers 169198 당구 연습
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/169198
"""

import sys
input = sys.stdin.readline


def solution(m, n, startX, startY, balls):
    answer = []

    for ballX, ballY in balls:
        tmp = []

        for x, y in ((-ballX, ballY), (ballX, -ballY), (2*m-ballX, ballY), (ballX, 2*n-ballY)):
            if startX == ballX:
                if startY > ballY > y or startY < ballY < y:
                    continue
            elif startY == ballY:
                if startX > ballX > x or startX < ballX < x:
                    continue

            tmp.append((startX-x)**2 + (startY-y)**2)
        answer.append(min(tmp))

    return answer


if __name__ == "__main__":

    # m, n, startX, startY = map(int, input().split())

    m, n, startX, startY = 10, 10, 3, 7
    balls = [[7, 7], [2, 7], [7, 3]]

    print(solution(m, n, startX, startY, balls))