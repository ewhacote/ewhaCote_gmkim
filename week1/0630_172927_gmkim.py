"""
Programmers 172927 광물 캐기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/172927
"""

import sys
input = sys.stdin.readline

def solution(picks, minerals):

    answer = 0
    minerals = minerals[:min(len(minerals), sum(picks)*5)]

    fatigue = [[0, 0, 0] for x in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            fatigue[i // 5][0] += 1
        elif minerals[i] == "iron":
            fatigue[i // 5][1] += 1
        else:
            fatigue[i // 5][2] += 1

    sorted_fatigue = sorted(fatigue, key=lambda x: (-x[0], -x[1], -x[2]))

    for mineral in sorted_fatigue:
        dia, iron, stone = mineral
        for i in range(len(picks)):
            if i == 0 and picks[i] > 0:
                answer += dia + iron + stone
                picks[i] -= 1
                break
            elif i == 1 and picks[i] > 0:
                answer += 5 * dia + iron + stone
                picks[i] -= 1
                break
            elif i == 2 and picks[i] > 0:
                answer += 25 * dia + 5 * iron + stone
                picks[i] -= 1
                break

    return answer

if __name__ == "__main__":

    picks = list(map(int, input().split()))
    minerals = list(map(str, input().split()))

    print(solution(picks, minerals))