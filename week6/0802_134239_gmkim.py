"""
Programmers 134239 우박수열 정적분
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/134239
"""

import sys
input = sys.stdin.readline

def solution(k, ranges):
    answer = []
    arr = []

    while k != 1:
        arr.append(k)
        k = k / 2 if k % 2 == 0 else k * 3 + 1
    arr.append(k)

    for r in ranges:
        total = 0
        tmp_arr = arr[r[0] : len(arr)+r[1]]

        if r[0] >= r[1] + len(arr):
            answer.append(-1)
            continue

        for i in range(len(tmp_arr)-1):
            total += ((tmp_arr[i] + tmp_arr[i+1])/2)

        answer.append(total)

    return answer


if __name__ == "__main__":

    k = int(input())
    ranges = list(map(int, input().split()))

    print(solution(k, ranges))