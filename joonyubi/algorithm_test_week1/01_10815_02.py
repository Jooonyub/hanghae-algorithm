#숫자카드

import sys
from collections import deque
import time
r = sys.stdin.readline

'''
N = 5                                       #첫번째 입력(입력할 숫자 N)
N_list = set(6, 3, 2, 10, -10)              #두번째 입력(N개 숫자의 원소들) -> N_list라는 집합으로 묶어서 저장
M = 8                                       #세번째 입력(비교할 수의 개수 M)
checknumlist = [10, 9, -5, 2, 3, 4, 5, -10] #네번째 입력(비교할 수의 목록) -> checknum_list라는 리스트에 저장
checknum_queue = deque()                    #checknum_list의 값들을 옮길 queue 초기화
checknum_queue.extend(checknumlist)         #입력받은 체크할 숫자목록을 queue에 추가(extend 메서드)
'''

N = int(r())                                #N : 상근이가 가지고 있는 숫자카드 개수
N_list = set(map(int, r().split()))         #N_list : 상근이가 가지고 있는 숫자카드의 정수 세트
M = int(r())                                #M : 1~500,000 사이의 정수

checknumlist = list(map(int, r().split()))  #네번째 입력(비교할 수의 목록) -> checknum_list라는 리스트에 저장
checknum_queue = deque()                        #checknum_list의 값들을 옮길 queue 초기화
checknum_queue.extend(checknumlist)             #입력받은 체크할 숫자목록을 queue에 추가(extend 메서드)

start = time.time()                         #for 코드 실행에 걸리는 시간 측정

while checknum_queue:                       #queue의 원소가 하나도 남지 않게 되면 while 반복문이 종료된다.
    if checknum_queue.popleft() in N_list:  #queue의 가장 첫번째 값이 N_list에 존재하는지 판별
        print('1', end=' ')                 #True일 경우 -> 1을 출력
    else:
        print('0', end= ' ')                #False일 경우 -> 0을 출력

end = time.time()                           #for 코드 실행에 걸리는 시간 측정
print('time record:', end-start)            #for 코드 실행에 걸리는 시간 측정





'''
for i in range(len(checknumlist)):
    if checknumlist[i] in N_list:
        print('1', end=' ')
        #result.append(1)
    else:
        print('0', end=' ')
        #result.append(0)

    #print(result[i], end=' ')
'''


'''
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

예제 입력 1 
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
예제 출력 1 
1 0 0 1 1 0 0 1
'''
