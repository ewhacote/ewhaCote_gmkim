"""
Programmers 172927 연속된 부분 수열의 합
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/178870
"""

import sys
input = sys.stdin.readline

def solution(sequence, k):
    answer = []
    end = cnt = 0

    for start in range(len(sequence)):
        
        while end < len(sequence) and cnt < k:
            cnt += sequence[end]
            end += 1

        if cnt == k:
            if not answer:
                answer = [start, end - 1]
            else:
                if answer[1] - answer[0] > end - 1 - start:
                    answer = [start, end - 1]

        cnt -= sequence[start]

    return answer

if __name__ == "__main__":

    sequence = list(map(int, input().split()))
    k = int(input())

    print(solution(sequence, k))