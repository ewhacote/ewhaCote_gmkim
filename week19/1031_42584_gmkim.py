"""
Programmers 42584 주식가격
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42584
"""

import sys
from collections import deque
input = sys.stdin.readline


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer

if __name__ == "__main__":

    prices = list(map(int, input().split()))

    print(solution(prices))