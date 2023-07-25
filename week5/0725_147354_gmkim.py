"""
Programmers 147354 테이블 해시 함수
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/147354
"""

import sys
input = sys.stdin.readline

def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key = lambda x: [x[col - 1], -x[0]])

    for i in range(row_begin, row_end + 1):
        total = 0

        for j in data[i - 1]:
            total += (j % i)

        answer ^= total

    return answer

if __name__ == "__main__":

    data = list(map(int, input().split()))
    col, row_begin, row_end = map(int, input().split())

    print(solution(data, col, row_begin, row_end))