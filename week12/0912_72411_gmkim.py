"""
Programmers 72411 메뉴 리뉴얼
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/72411
"""

import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline

def solution(orders, course):
    answer = []

    for c in course:
        temp = []

        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi

        counter = Counter(temp)

        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)

if __name__ == "__main__":

    orders = list(map(str, input().split()))
    course = list(map(int, input().split()))

    print(solution(orders, course))