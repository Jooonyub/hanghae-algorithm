#deque 이해하기

from collections import deque

'''
에러를 계속 겪은 부분
- deque의 처음 선언 시 값을 어떻게 입력받을 것인가?
입력값 : string type
list 입력시 자주 쓰던 방식
    ls = list(map(int, sys.stdin.readline().split))
    예를 들어 "10 9 -5 2 3 4 5 -10"
    이 된다.
'''


#ls = map(int,"10 9 -5 2 3 4 5 -10".split())
ls = [10, 9, -5, 2, 3, 4, 5, -10]
dq = deque()

#print(ls)
dq.extend(ls)
print(dq)

