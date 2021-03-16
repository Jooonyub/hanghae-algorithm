#0316_02_2108.py
#통계학

import sys
import math
import time
from collections import Counter
r = sys.stdin.readline

N = int(r())

def arithmetic_mean(n, num_list):
    return round(sum(num_list)/n)

def median(n, num_list):
    #num_list.sort()
    return num_list[n//2]

def mode(n, num_list):
    count = Counter(num_list).most_common() 
    if len(count) > 1 and count[0][1] == count[1][1]:
        return count[1][0]
    else:
        return count[0][0]
'''
def mode(n, num_list):

    cnt_max = 0
    most_nums = []

    #num_list.sort()
    #num_set = set(num_list.sort())
    count_info = {}
    for i in range(n):
        if num_list[i] not in count_info.keys():
            count_info[num_list[i]] = num_list.count(num_list[i])
    #여기까지하면 dict에 오름차순의 숫자별 빈도를 담은 dict 담김

    cnt_max = max(count_info.values())

    for num in count_info.keys():
        if count_info[num] == cnt_max:
            most_nums.append(num)
    #most_nums.append(num) if num == cnt_max for num in count_info.keys() 

    if len(most_nums) > 1:
        return most_nums[1]
    else:
        return most_nums[0]
'''
'''
def mode(n, num_list):

    cnt_max = 0
    most_nums = []
    num_list.sort()
    num_set = set(num_list.sort())
    num_set_cnt = []


    list_num_set = list(num_set)
    for num in list_num_set:
        num_set_cnt.append(num_list.count(num))

    cnt_max = max(num_set_cnt)
    num_modes = num_set_cnt.count(cnt_max)

    for i in range(len(list_num_set)):
        if num_list.count(list_num_set[i]) == cnt_max:
            most_nums.append(list_num_set[i])

    if num_modes == 1:
        return most_nums[0]
    else:
        return most_nums[1]
'''
'''
def mode(n, num_list):
    cnt_max = 0
    most_nums = []
    num_list.sort()
    num_set = set(num_list)
    num_set_cnt = []
    list_num_set = list(num_set)
    for num in list_num_set:
        num_set_cnt.append(num_list.count(num))
    cnt_max = max(num_set_cnt)
    num_modes = num_set_cnt.count(cnt_max)
    if num_modes == 1:
        return list_num_set[-1]
    else:
        return list_num_set[-2]
'''

'''
def mode(n, num_list):
    cnt_max = 0
    most_num = None
    num_list.sort()
    num_set = set(num_list)
    for num in list(num_set):
        if cnt_max < num_list.count(num):
            cnt_max = num_list.count(num)
            most_num = num
    #최빈값이 여러개인 경우
    if 
    for i in num_list:
        if num_list.count(i) == cnt_max:
            if i not in most_nums:
                most_nums.append(i)
    if len(most_nums) >1:
        return most_nums[1]
    else:
        return most_nums[0]
'''

def scope(n, num_list):
    return max(num_list) - min(num_list)

numbers = []
for _ in range(N):
    numbers.append(int(r()))
numbers.sort()

time1 = time.time()
print(arithmetic_mean(N, numbers))
time2 = time.time()
print(median(N, numbers))
time3 = time.time()
print(mode(N, numbers))
time4 = time.time()
print(scope(N, numbers))
time5 = time.time()

#print("arithmetic:",time2-time1)
#print("median:",time3-time2)
#print("mode:",time4-time3)
#print("scope",time5-time4)

#print("total:",time5-time1)


'''
통계학 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	43783	10419	8541	26.631%
문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 
단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

예제 입력 1 
5
1
3
8
-2
2
예제 출력 1 
2
2
1
10
예제 입력 2 
1
4000
예제 출력 2 
4000
4000
4000
0
예제 입력 3 
5
-1
-2
-3
-1
-2
예제 출력 3 
-2
-2
-1
2
'''