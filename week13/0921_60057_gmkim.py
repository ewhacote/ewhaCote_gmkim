"""
Programmers 60057 문자열 압축
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""

import sys
input = sys.stdin.readline

def solution(s):

    min_len = len(s)

    for unit in range(1, (len(s)//2)+1):

        result = ""
        previous = s[0:unit]
        count = 1

        for idx in range(unit, len(s), unit):

            now = s[idx:idx+unit]

            if (now == previous):
                count += 1
            else:
                if (count >= 2):
                    result += str(count) + previous
                else:
                    result += previous
                previous = now
                count = 1

        if (count >= 2):
            result += str(count) + previous
        else:
            result += previous

        min_len = min(min_len, len(result))

    return min_len

if __name__ == "__main__":

    s = str(input())

    print(solution(s))