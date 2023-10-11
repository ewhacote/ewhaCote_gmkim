"""
Programmers 49993 스킬트리
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/49993
"""

import sys
input = sys.stdin.readline

def solution(skill, skill_trees):
    answer = 0

    for sk in skill_trees:
        tmp = ''
        for s in sk:
            if s in skill:
                tmp += s

        if tmp == skill[:len(tmp)]:
        	answer += 1

    return answer

if __name__ == "__main__":

    skill = str(input())
    skill_trees = list(map(str, input().split()))

    print(solution(skill, skill_trees))