#0315_01_11050.py
#이항계수 1

import sys
n, k = map(int, sys.stdin.readline().split())

bunmo = 1
bunza = 1
for i in range(1,k+1):
    bunza *= n-(i-1)
    bunmo *= i

binomial = int(bunza/bunmo)
print(binomial)



'''
5
1
5/1

5
2
5*4/2*1

5
3
5*4*3/3*2*1
'''

'''
이항 계수 1 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	19134	12272	10657	64.796%

문제
자연수 N과 정수K 가 주어졌을 때 이항 계수 (N \n K)
를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

출력
 
(N \n K)를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10
'''