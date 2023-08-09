"""
Programmers 131701 연속 부분 수열 합의 개수
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131701
"""

import sys
input = sys.stdin.readline

def solution(elements):
    answer = set()
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.add(sum((elements*2)[i:i+j]))
    return len(answer)

if __name__ == "__main__":

    elements = list(map(int, input().split()))

    print(solution(elements))