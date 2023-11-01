"""
Programmers 42583 다리를 지나는 트럭
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42583
"""

import sys
import collections import deque
input = sys.stdin.readline

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    cur_weight = 0
    while len(truck_weights) != 0:
        answer += 1
        cur_weight -= bridge.popleft()

        if cur_weight + truck_weights[0] <= weight:
            cur_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

    answer += bridge_length

    return answer

if __name__ == "__main__":

    bridge_length = int(input())
    weight = int(input())
    truck_weights = list(map(int, input().split()))

    print(solution(bridge_length, weight, truck_weights))