"""
Programmers 148653 마법의 엘리베이터
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/148653
"""

import sys
input = sys.stdin.readline

def solution(storey):
    answer = 0

    while storey:
        num = storey % 10

        if num > 5:
            answer += (10 - num)
            storey += 10

        elif num < 5:
            answer += num

        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += num

        storey //= 10

    return answer

if __name__ == "__main__":

    storey = int(input())

    print(solution(storey))