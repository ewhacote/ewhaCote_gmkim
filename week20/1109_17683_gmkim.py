"""
Programmers 17683 방금그곡
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/17683
"""

import sys
input = sys.stdin.readline

def time_c(t):
    return int(t.split(':')[0])*60 + int(t.split(':')[1])

def change(x):
    exc = {'C#':'1','D#':'2', 'F#':'3', 'G#':'4', 'A#':'5'}
    for k, v in exc.items():
        x = x.replace(k, v)
    return x

def solution(m, musicinfos):
    answer = []
    for info in musicinfos:
        info = info.split(',')
        info[3] = change(info[3])
        T = time_c(info[1]) - time_c(info[0])

        if T >= len(info[3]):
            M = info[3] * (T//len(info[3])) + info[3][:T%len(info[3])]
        else:
            M = info[3][:T]

        if change(m) in M:
            answer.append([T, info[2]])

    if len(answer) == 0:
        return '(None)'
    else:
        return sorted(answer, key=lambda x: -x[0])[0][1]

if __name__ == "__main__":

    m = str(input())
    musicinfos = list(map(str, input().split()))

    print(solution(m, musicinfos))