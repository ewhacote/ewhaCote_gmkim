"""
Programmers 131130 혼자 놀기의 달인
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131130
"""

import sys
input = sys.stdin.readline

def solution(cards):
    answer = []
    visited = [False] * (len(cards)+1)

    for v in cards:
        if not visited[v]:
            tmp = []

            while v not in tmp:
                tmp.append(v)
                v = cards[v-1]
                visited[v] = True

            answer.append(len(tmp))

    if answer[0] == len(cards):
        return 0

    else:
        answer.sort(reverse=True)

    return answer[0] * answer[1]

if __name__ == "__main__":

    cards = list(map(int, input().split()))

    print(solution(cards))