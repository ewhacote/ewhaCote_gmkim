"""
Programmers 84512 모음 사전
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/84512
"""

import sys
from itertools import product
input = sys.stdin.readline

def solution(word):
    answer = []
    w_list = ['A', 'E', 'I', 'O', 'U']

    for i in range(1,6):
        for per in product(w_list,repeat = i):
            answer.append(''.join(per))

    answer.sort()
    return answer.index(word)+1

if __name__ == "__main__":

    word = str(input())

    print(solution(word))