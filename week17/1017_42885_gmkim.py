"""
Programmers 42885 구명보트
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""

import sys
input = sys.stdin.readline

def solution(people, limit):

    count = 0
    people.sort()
    start, end = 0, len(people)-1

    while start <= end:
        count += 1

        if (people[start] + people[end] <= limit):
            start += 1
            end -= 1
        else:
            end -= 1

    return count

if __name__ == "__main__":

    people = list(map(int, input().split()))
    limit = int(input())

    print(solution(people, limit))