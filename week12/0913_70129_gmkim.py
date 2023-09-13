"""
Programmers 70129 이진 변환 반복하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/70129
"""

import sys
input = sys.stdin.readline

def solution(s):
    del_0, cnt = 0, 0

    while s != '1':
        del_0 += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        cnt += 1

    return [cnt, del_0]

if __name__ == "__main__":

    s = str(input())

    print(solution(s))