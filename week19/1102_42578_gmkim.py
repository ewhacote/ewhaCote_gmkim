"""
Programmers 42578 의상
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""

import sys
input = sys.stdin.readline

def solution(clothes):

    answer = 1
    hash_map = {}

    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1

    for type in hash_map:
        answer *= (hash_map[type] + 1)

    return answer - 1

if __name__ == "__main__":

    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

    print(solution(clothes))