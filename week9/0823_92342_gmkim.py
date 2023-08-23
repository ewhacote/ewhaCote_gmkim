"""
Programmers 92342 양궁대회
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/92342
"""

def solution(n, info):
    answer = []
    ryan = [0]*11
    diff = 0

    def dfs(m, idx):
        nonlocal answer, diff, ryan

        if m == n:
            r, a = 0, 0

            for j in range(11):
                if ryan[j] > info[j]:
                    r += 10-j
                elif 0 != info[j] and ryan[j] <= info[j]:
                    a += 10-j

            if r > a:
                if diff < r - a:
                    diff = r - a
                    answer = ryan[:]

                elif diff == r - a:
                    for i in range(10, -1, -1):
                        if ryan[i] < answer[i]:
                            break
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
            return

        for i in range(idx, 11):
            ryan[i] += 1
            dfs(m+1, i)
            ryan[i] -= 1


    dfs(0, 0)

    return answer if answer else [-1]

if __name__ == "__main__":

    n = int(input())
    info = list(map(int, input().split()))

    print(solution(n, info))