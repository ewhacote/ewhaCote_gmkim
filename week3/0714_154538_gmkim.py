"""
Programmers 154538 숫자 변환하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154538
"""

import sys
input = sys.stdin.readline

def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer

        nxt = set()

        for i in s:
            if i+n <= y:
                nxt.add(i+n)
            if i*2 <= y:
                nxt.add(i*2)
            if i*3 <= y:
                nxt.add(i*3)
        s = nxt
        answer+=1

    return -1

if __name__ == "__main__":

    x, y, n = map(int, input().split())

    print(solution(x, y, n))