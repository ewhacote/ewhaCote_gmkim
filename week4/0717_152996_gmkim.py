"""
Programmers 152996 시소 짝꿍
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/152996
"""

import sys
from collections import Counter
input = sys.stdin.readline

def solution(weights):
    answer = 0
    weight_cnt = Counter(weights)

    for key, value in weight_cnt.items():
        if value >= 2:
            answer += value *(value-1)//2

    weights = list(set(weights))

    for weight in weights:
        for ratio in [1/2, 2/3, 3/4]:
            if weight * ratio in weights:
                answer += weight_cnt[weight] * weight_cnt[weight * ratio]

    return answer

if __name__ == "__main__":

    weights = list(map(int, input().split()))

    print(solution(weights))