"""
Programmers 42890 후보키
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42890
"""

import sys
from itertools import combinations as cbn
input = sys.stdin.readline

def solution(relation):
    answer = set()
    row, col = len(relation), len(relation[0])

    candidates = []
    for i in range(1, col+1):
        candidates.extends(cbn(range(col), i))

    unique = []
    for candi in candidates:
        tmp = [tuple([item[i] for i in candi]) for item in relation]

        if len(set(tmp)) == row:
            unique.append(candi)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)

if __name__ == "__main__":

    relation = list(map(str, input().split()))

    print(solution(relation))