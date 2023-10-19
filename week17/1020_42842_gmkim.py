"""
Programmers 42842 카펫
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842
"""

import sys
input = sys.stdin.readline

def solution(brown, yellow):

    for i in range(1, yellow+1):
        if (yellow % i == 0):
            y_row, y_col = yellow / i, i

            if ((y_row + y_col) * 2 + 4 == brown):
                return [y_row+2, y_col+2]

if __name__ == "__main__":

    brown, yellow = map(int, input().split())

    print(solution(brown, yellow))