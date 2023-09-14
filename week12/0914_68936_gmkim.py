"""
Programmers 68936 쿼드압축 후 개수 세기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/68936
"""

import sys
input = sys.stdin.readline

def solution(arr):
    answer = [0, 0]

    def comp(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):

                if arr[i][j] != init:
                    nn = n // 2
                    comp(x, y, nn)
                    comp(x, y + nn, nn)
                    comp(x + nn, y, nn)
                    comp(x + nn, y + nn, nn)
                    return

        answer[init] += 1

    comp(0, 0, len(arr))
    return answer

if __name__ == "__main__":

    arr = list(map(int, input().split()))

    print(solution(arr))