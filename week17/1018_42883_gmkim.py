"""
Programmers 42883 구명보트
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""

import sys
input = sys.stdin.readline

def solution(number, k):
    answer = []

    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

if __name__ == "__main__":

    number = str(input())
    k = int(input())

    print(solution(number, k))