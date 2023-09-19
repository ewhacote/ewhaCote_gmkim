"""
Programmers 64065 튜플
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/64065
"""

import sys
input = sys.stdin.readline

def solution(s):
    ls = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)
    result = []

    for l in ls:
        for s in l:
            if int(s) not in result:
                result.append(int(s))
                break

    return result

if __name__ == "__main__":

    s = str(input())

    print(solution(s))