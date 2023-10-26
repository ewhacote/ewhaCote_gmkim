"""
Programmers 42626 더 맵게
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42626
"""

import sys, heapq
input = sys.stdin.readline

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        else:
            x, y = heapq.heappop(scoville), heapq.heappop(scoville)
            heapq.heappush(scoville, x + y * 2)

            answer += 1

    return answer

if __name__ == "__main__":

    scoville = list(map(int, input().split()))
    K = int(input())

    print(solution(scoville, K))