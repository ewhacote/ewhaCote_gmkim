"""
Programmers 17684 압축
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17684
"""

import sys
input = sys.stdin.readline

def solution(msg):
    answer = []
    dict = {}
    
    for e in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        dict[e] = len(dict) + 1
    
    cur = ""
    for i in range(len(msg)):
        cur += msg[i]
        if i + 1 >= len(msg) or (cur + msg[i + 1] not in dict):
            answer.append(dict[cur])
            if i + 1 >= len(msg):
                dict[cur] = len(dict) + 1
            else:
                dict[cur + msg[i + 1]] = len(dict) + 1
            cur = ""
    
    return answer

if __name__ == "__main__":

    msg = str(input())

    print(solution(msg))