"""
Programmers 77885 2개 이하로 다른 비트
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77885
"""

import sys
input = sys.stdin.readline

def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)

        else:
            num = format(num, 'b')

            if not '0' in num:
                answer.append(int('10' + num[1:], 2))
            else:
                idx = num.rfind('0')
                answer.append(int(num[:idx] + '10' + num[idx+2:], 2))

    return answer

if __name__ == "__main__":

    numbers = list(map(int, input().split()))

    print(solution(numbers))