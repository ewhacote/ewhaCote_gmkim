"""
Programmers 150368 이모티콘 할인행사
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/150368
"""

import sys
input = sys.stdin.readline

def solution(users, emoticons):
    answer = [0, 0]
    data = [10 ,20, 30, 40]
    discount = []

    def dfs(temp, depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d

    dfs([0] * len(emoticons), 0)

    for d in range(len(discount)):
        join, price = 0, [0] * len(users)

        for e in range(len(emoticons)):
            for u in range(len(users)):
                if users[u][0] <= discount[d][e]:
                    price[u] += emoticons[e] * (100 - discount[d][e]) / 100

        for u in range(len(users)):
            if price[u] >= users[u][1]:
                join += 1
                price[u] = 0

        if join >= answer[0]:
            if join == answer[0]:
                answer[1] = max(answer[1], sum(price))
            else:
                answer[1] = sum(price)

            answer[0] = join


    return answer

if __name__ == "__main__":

    users = list(map(int, input().split()))
    emoticons = list(map(int, input().split()))

    print(solution(users, emoticons))