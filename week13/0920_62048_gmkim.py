"""
Programmers 62048 멀쩡한 사각형
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/62048
"""

import sys, math
input = sys.stdin.readline

def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))

if __name__ == "__main__":

    w, h = map(int, input().split())

    print(solution(w,h))