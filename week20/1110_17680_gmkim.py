"""
Programmers 17680 캐시
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""

import sys
input = sys.stdin.readline

def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city in cities:
        city = city.lower()
        if cacheSize:
            if not city in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                answer += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
        else:
            answer += 5
    return answer

if __name__ == "__main__":

    cacheSize = int(input())
    cities = list(map(str, input().split()))

    print(solution(cacheSize, cities))
