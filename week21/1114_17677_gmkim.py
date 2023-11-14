"""
Programmers 17677 뉴스 클러스터링
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17677
"""

import sys
input = sys.stdin.readline

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    A, B = [], []

    for i in range(len(str1)-1):
        str = str1[i:i+2]

        if str.isalpha():
            A.append(str)

    for i in range(len(str2)-1):
        str = str2[i:i+2]

        if str.isalpha():
            B.append(str)

    if len(A) == 0 and len(B) == 0:
        j = 1

    else:
        a_temp = A.copy()
        a_result = A.copy()

        for i in B:

            if i not in a_temp:
                a_result.append(i)
            else:
                a_temp.remove(i)

        result = []

        for i in B:
            if i in A:
                A.remove(i)
                result.append(i)

        j = len(result)/len(a_result)

    return (int(j * 65536))

if __name__ == "__main__":

    str1, str2 = map(str, input().split())

    print(solution(str1, str2))