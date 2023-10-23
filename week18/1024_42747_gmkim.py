"""
Programmers 42747 H-Index
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""

import sys
input = sys.stdin.readline

def solution(citations):
    citations = sorted(citations)
    n = len(citations)

    for i in range(n):
        if citations[i] >= n-i:
            return n-i

    return 0

if __name__ == "__main__":

    citations = list(map(int, input().split()))

    print(solution(citations))