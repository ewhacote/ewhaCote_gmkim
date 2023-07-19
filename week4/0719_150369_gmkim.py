"""
Programmers 150369 택배 배달과 수거하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/150369
"""

import sys
input = sys.stdin.readline

def solution(cap, n, deliveries, pickups):
    d, p = 0, 0
    answer = 0

    for i in range(n):
        d += deliveries[n-i-1]
        p += pickups[n-i-1]

        while p > 0 or d > 0:
            d -= cap
            p -= cap
            answer += 2 * (n-i)

    return answer

if __name__ == "__main__":

    cap, n = map(int, input().split())
    deliveries = list(map(int, input().split()))
    pickups = list(map(int, input().split()))

    print(solution(cap, n, deliveries, pickups))