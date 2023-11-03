"""
Programmers 42577 전화번호 목록
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""

import sys
input = sys.stdin.readline

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer

if __name__ == "__main__":

    phone_book = list(map(str, input().split()))

    print(solution(phone_book))