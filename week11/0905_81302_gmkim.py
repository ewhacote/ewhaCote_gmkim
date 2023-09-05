"""
Programmers 81302 거리두기 확인하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/81302
"""

import sys
input = sys.stdin.readline

def check_distance(place):
    plist = [(y, x) for y in range(5) for x in range(5) if place[y][x] == 'P']

    for y, x in plist:
        for y2, x2 in plist:
            dist = abs(y-y2) + abs(x-x2)
            if dist == 0 or dist > 2:
                continue

            if dist == 1:
                return 0
            elif y == y2 and place[y][int((x+x2)/2)] != 'X':
                return 0
            elif x == x2 and place[int((y+y2)/2)][x] != 'X':
                return 0
            elif y != y2 and x != x2:
                if place[y2][x] != 'X' or place[y][x2] != 'X':
                    return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(check_distance(place))

    return answer

if __name__ == "__main__":

    places = list(map(str, input().split()))

    print(solution(places))