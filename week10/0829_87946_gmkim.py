"""
Programmers 87390 n^2 배열 자르기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87390
"""

import sys
from itertools import permutations
input = sys.stdin.readline

def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        a = i//n # 몫
        b = i%n #나머지
        if a<b: a,b =b,a 큰거 구하기
        answer.append(a+1)

    return answer

if __name__ == "__main__":

    n, left, right = map(str, input().split())

    print(solution(n, left, right))