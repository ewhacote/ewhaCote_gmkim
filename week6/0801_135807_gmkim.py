"""
Programmers 135807 숫자 카드 나누기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/135807
"""

import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def notDiv(array, gcd):
    for n in array:
        if n % gcd == 0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0

    gcdA = arrayA[0]
    gcdB = arrayB[0]

    for n in arrayA[1:]:
        gcdA = gcd(n, gcdA)

    for n in arrayB[1:]:
        gcdB = gcd(n, gcdB)

    if notDiv(arrayA, gcdB):
        answer = max(answer, gcdB)

    if notDiv(arrayB, gcdA):
        answer = max(answer, gcdA)

    return answer


if __name__ == "__main__":

    arrayA = list(map(int, input().split()))
    arrayB = list(map(int, input().split()))

    print(solution(arrayA, arrayB))