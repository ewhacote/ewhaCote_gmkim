"""
Programmers 42860 조이스틱
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42860
"""

import sys
input = sys.stdin.readline

def solution(name):

    spell_move, cursor_move = 0, len(name) - 1

    for i, spell in enumerate(name):
        spell_move += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        next = i + 1

        while next < len(name) and name[next] == 'A':
            next += 1

        cursor_move = min([ cursor_move, 2 * i + len(name) - next, i + 2 * (len(name) - next) ])

    return spell_move + cursor_move

if __name__ == "__main__":

    name = str(input())

    print(solution(name))