"""
Programmers 67257 수식 최대화
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/67257
"""

import sys
input = sys.stdin.readline

def solution(expression):
  operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')] 
  answer = [] 
  
  for op in operations: 
    a = op[0] b = op[1] 
    temp_list = [] 
    
    for e in expression.split(a): 
      temp = [f"({i})" for i in e.split(b)] 
      temp_list.append(f'({b.join(temp)})') 
      
    answer.append(abs(eval(a.join(temp_list)))) 
      
  return max(answer)

if __name__ == "__main__":

    expression = str(input())

    print(solution(expression))
