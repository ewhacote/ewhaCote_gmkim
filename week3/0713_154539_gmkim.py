"""
Programmers 154539 뒤에 있는 큰 수 찾기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154539
"""

import sys
input = sys.stdin.readline

def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer

if __name__ == "__main__":

    numbers = list(map(int, input().split()))

    print(solution(numbers))