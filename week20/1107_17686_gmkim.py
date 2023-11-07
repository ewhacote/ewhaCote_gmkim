"""
Programmers 17686 파일명 정렬
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17686
"""

import sys, re
input = sys.stdin.readline

def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))

    return [''.join(s) for s in sort]

if __name__ == "__main__":

    files = list(map(int, input().split()))

    print(solution(files))