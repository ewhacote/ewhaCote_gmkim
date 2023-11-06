"""
Programmers 17687 n진수 게임
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17687
"""

import sys
input = sys.stdin.readline

def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)

    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]

def solution(n, t, m, p):
    answer = ''
    test = ''

    for i in range(m*t):
        test += str(convert(i, n))

    while len(answer) < t:
        answer += test[p-1]
        p += m

    return answer

if __name__ == "__main__":

    n, t, m, p = map(int, input().split())

    print(solution(n, t, m, p))