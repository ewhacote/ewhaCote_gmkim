"""
Programmers 76502 괄호 회전하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/76502
"""

import sys
from collections import deque
input = sys.stdin.readline

def check(s):

    while True:
        if "()" in s:
            s=s.replace("()","")
        elif "[]" in s:
            s=s.replace("[]","")
        elif "{}" in s:
            s=s.replace("{}","")
        else:
            break

    return False if s else True

def solution(s):
    answer = 0

    for i in range(len(s)):
        answer += check(s)
        s = s[1:] + s[0]

    return answer

if __name__ == "__main__":

    s = str(input())

    print(solution(s))