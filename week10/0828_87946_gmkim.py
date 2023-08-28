"""
Programmers 87946 피로도
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""

import sys
from itertools import permutations
input = sys.stdin.readline

def solution(k, dungeons):
    d_num = len(dungeons)
    answer = []

    for permute in permutations(dungeons, d_num):
        limit = k
        cnt = 0

        for pm in permute:
            if limit >= pm[0]:
                limit -= pm[1]
                cnt += 1
        answer.append(cnt)

    return max(answer)

if __name__ == "__main__":

    k = int(input())
    dungeons = list(map(str, input().split()))

    print(solution(k, dungeons))