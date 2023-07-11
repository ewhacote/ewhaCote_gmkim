"""
Programmers 155651 호텔 대실
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/155651
"""

import sys, heapq
input = sys.stdin.readline

def solution(book_time):
    answer = 1
    heap = []

    total_min = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    total_min.sort()

    for s, e in total_min:
        if not heap:
            heapq.heappush(heap, e)
            continue

        if heap[0] <= s:
            heapq.heappop(heap)
        else:
            answer += 1

        heapq.heappush(heap, e + 10)

    return answer

if __name__ == "__main__":

    # book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
    # book_time = [["09:10", "10:10"], ["10:20", "12:20"]]
    book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]

    print(solution(book_time))