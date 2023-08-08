"""
Programmers 131704 택배상자
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131704
"""

import sys
from collections import Counter
input = sys.stdin.readline

def solution(order):
    answer = 0
    tmp = []
    i = 1

    while i != len(order)+1:
        tmp.append(i)
        while tmp[-1] == order[answer]:
            answer += 1
            tmp.pop()
            if len(tmp) == 0:
                break
        i += 1
    return answer

if __name__ == "__main__":

    order = list(map(int, input().split()))

    print(solution(order))