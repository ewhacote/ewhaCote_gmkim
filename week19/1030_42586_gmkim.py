"""
Programmers 42586 기능개발
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""

import sys, math
input = sys.stdin.readline

def solution(progresses, speeds):
    answer = []
    progress_day = [math.ceil((100 - x) / y) for x, y in zip(progresses, speeds)]
    count = 0

    for i in progress_day:
        if i > count:
            answer.append(1)
            count = i
        else:
            answer[-1] += 1

    return answer

if __name__ == "__main__":

    progresses = list(map(int, input().split()))
    speeds = list(map(int, input().split()))

    print(solution(progresses, speeds))