#0313_04_1149.py
#RGB거리(다이나믹 프로그래밍)


#N번째 집에 대해서 발생하는 최소비용
#N-1번째 집에 어느 색이 칠해져있는지 저장되어있으면 그 색에 대한 인덱스를 제외한 나머지 두 비용중 최소값 더하기

import sys
N = int(sys.stdin.readline())       #첫째줄 입력값 -> 집의 수 N

#인덱스를 표시해놓음과 동시에 직전 인덱스에 따라 현재 최소값이 바뀔 수 있는 상황
memo = {} #값 2개를 저장한다면? 하나는 index, 다른 하나는 해당 index에 대한 cost

'''
memo = {
    1: (rgb_index_1, min_cost_1)
    2: (rgb_index_2, min_cost_2)
    .
    .
    .
} #값 2개를 저장한다면? 하나는 index, 다른 하나는 해당 index에 대한 cost
'''
'''
rgb_cost = list(map(int, sys.stdin.readline().split()))
    
#초기조건은 따로 입력해보기
                                     #초기조건. record에 아무런 값도 없을 때
minimum_1 = min(rgb_list)                     #입력받은 세 값중에서 최소비용의 값 찾아 minimum에 저장
index_minimum = rgb_list.index(minimum_1)     #index로 minimum값의 인덱스인지 찾기
record[1] = (index_minimum, minimum_1)                #key = N, value = index_minimum 설정
return index_minimum, minimum_1
'''

#minimum_indices = []
def cost(n, memo_cost):
    #index_minimum = None
    rgb_cost = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        rgb_index = rgb_cost.index(min(rgb_cost))
        min_cost = min(rgb_cost)
    if n in memo_cost:
        return memo_cost[n][1]
        #return memo_cost[N][0], memo_cost[N][1]
    else:
        tmp_cost = rgb_cost
        del tmp_cost[memo_cost[n-1][1]]
        min_cost = min(rgb_cost)
        rgb_index = rgb_cost.index(min_cost) 
        memo_cost[n] = (rgb_index, min_cost)
        return memo_cost[n-1][1] + memo_cost[n-2][1]


    if not memo_cost[n]:
        memo_cost[n-1][0]의 인덱스를 해당 rgb_cost에서 제외. 제외한 값중 최소값을 찾고, 최소값에 해당하는 인덱스를 다시 표시
        memo_cost[n] = 


    '''
    if N == 1:                                      #초기조건. record에 아무런 값도 없을 때
        minimum = min(rgb_list)                     #입력받은 세 값중에서 최소비용의 값 찾아 minimum에 저장
        index_minimum = rgb_list.index(minimum)     #index로 minimum값의 인덱스인지 찾기
        record[N] = (index_minimum, minimum)                   #key = N, value = index_minimum 설정
        return rgb_list[index_minimum]
    
    if N in index_record:
        return index_record[N][1]
    
    
    index_N = index(N-1, index_record)
    index_record[N] = index_N
    return index(N-1, index_record), index
    '''

print(cost(N, memo))


'''
N = 3
houses [{'r':26,'g':40,'b':83},{'r':49,'g':60,'b':57},{'r':13,'g':89,'b':99}] 

print(minimum_cost(houses))
'''

'''
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

예제 입력 1 
3
26 40 83
49 60 57
13 89 99
예제 출력 1 
96
'''