"""
Programmers 142085 디펜스 게임
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/142085
"""

import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, total_enemy = 0, 0
    heap = []

    for e in enemy:
        heappush(heap, -e)
        total_enemy += e

        if total_enemy > n:
            if k == 0: break
            total_enemy += heappop(heap)
            k -= 1

        answer += 1

    return answer

if __name__ == "__main__":

    n, k = map(int, input().split())
    enemy = list(map(int, input().split()))

    print(solution(n, k, enemy))