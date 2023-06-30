"""
Programmers 176962 과제 진행하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/176962
"""

import sys
from collections import deque
input = sys.stdin.readline

def convert_time(s) :
    h, m = map(int, s.split(':'))
    return h * 60 + m

def solution(plans):
    answer = []

    plans = [(name, convert_time(start), int(playtime)) for name, start, playtime in plans]
    plans.sort(key=lambda x: x[1])

    q = deque()
    time_left = 0

    for i in range(len(plans)):
        name, start, playtime = plans[i]

        while q:
            _name, _playtime = q.pop()
            if time_left >= _playtime:
                time_left -= _playtime
                answer.append(_name)
            else:
                q.append((_name, _playtime - time_left))
                break

        q.append((name, playtime))

        if i < len(plans) - 1:
            next_start = plans[i + 1][1]
            time_left = next_start - start

    while q:
        _name, _ = q.pop()
        answer.append(_name)

    return answer

if __name__ == "__main__":

    plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]

    print(solution(plans))