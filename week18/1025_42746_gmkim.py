"""
Programmers 42746 가장 큰 수
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42746
"""

import sys
input = sys.stdin.readline

def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num*3, reverse=True)

    return str(int(''.join(numbers_str)))

if __name__ == "__main__":

    numbers = list(map(int, input().split()))

    print(solution(numbers))