"""
Programmers 181187 두 원 사이의 정수 쌍
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181187
"""

import sys, math
input = sys.stdin.readline

def solution(r1, r2):
    answer = 0

    for i in range(1, r2 + 1):
        c1 = math.ceil(max(0, r1 ** 2 - i ** 2) ** 0.5)
        c2 = math.floor((r2 ** 2 - i ** 2) ** 0.5)

        answer += c2 - c1 + 1

    return answer * 4

if __name__ == "__main__":

    r1, r2 = map(int, input().split())

    print(solution(r1, r2))