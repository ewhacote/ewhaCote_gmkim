"""
Programmers 181188 요격 시스템
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181188?language=python3
"""

import sys
input = sys.stdin.readline

def solution(targets):
    answer = e = 0
    targets.sort(key=lambda x: (x[1], x[0]))

    for target in targets:
        if target[0] >= e:
            e = target[1]
            answer += 1

    return answer

if __name__ == "__main__":

    n = int(input())
    targets = [list(map(int, input().split())) for _ in range(n)]

    # given input
    # targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

    print(solution(targets))