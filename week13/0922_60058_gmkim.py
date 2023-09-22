"""
Programmers 60058 괄호 변환
문제 링크: hhttps://school.programmers.co.kr/learn/courses/30/lessons/60058
"""

import sys
input = sys.stdin.readline

def solution(p):
    if not p :
        return p

    r, c = True, 0
    for i in range(len(p)):
        c = c-1 if p[i] == '(' else c+1
        r = False if c>0 else r

        if c == 0:
            if r:
                return p[:i + 1] + solution(p[i + 1:])
            else:
                return '(' + solution(p[i + 1:]) + ')' + ''.join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))


if __name__ == "__main__":

    p = str(input())

    print(solution(p))