"""
Programmers 131127 할인 행사
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131127
"""

import sys
from collections import Counter
input = sys.stdin.readline

def solution(want, number, discount):
    check = len(discount) - 9
    days, start, end = 0, 0, 10

    for _ in range(check):
        days += 1
        counter = Counter(discount[start:end])

        for item, count in zip(want, number):
            if counter[item] != count:
                days -= 1
                break

        start += 1
        end += 1

    return days

if __name__ == "__main__":

    want = list(map(int, input().split()))
    number = list(map(int, input().split()))
    discount = list(map(int, input().split()))


    print(solution(want, number, discount))