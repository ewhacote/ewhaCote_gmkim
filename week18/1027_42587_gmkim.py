"""
Programmers 42587 프로세스
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587
"""

import sys
input = sys.stdin.readline

def solution(priorities, location):
    answer = 0
    queue =  [(i, p) for i, p in enumerate(priorities)]

    while True:
        cur = queue.pop(0)

        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

if __name__ == "__main__":

    priorities = list(map(int, input().split()))
    location = int(input())

    print(solution(priorities, location))