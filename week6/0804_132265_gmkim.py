"""
Programmers 132265 롤케이크 자르기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132265
"""

import sys
from collections import Counter
input = sys.stdin.readline

def solution(topping):
    answer = 0
    cnt = Counter(topping)
    set_cnt = set()

    for i in topping:
        cnt[i] -= 1
        set_cnt.add(i)

        if cnt[i] == 0:
            cnt.pop(i)

        if len(cnt) == len(set_cnt):
            answer += 1

    return answer

if __name__ == "__main__":

    topping = list(map(int, input().split()))

    print(solution(topping))