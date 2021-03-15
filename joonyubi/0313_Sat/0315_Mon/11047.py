#0315_01_11047.py
#동전 0

import sys
r = sys.stdin.readline

n, k = map(int, r().split())
coins = []

for i in range(n):
    coins.append(int(r()))

'''
#testcase1
n,k = 10, 4200
coins = [1,5,10,50,100,500,1000, 5000, 100000, 500000]

#testcase2
n, k = 10, 4790
coins = [1,5,10,50,100,500,1000, 5000, 100000, 500000]
'''
#print(coins)

coins.sort(reverse=True)
#print(coins)

valid_coins = [coin for coin in coins if coin < k]
#print(valid_coins)

count = 0
#coins_used = []
for coin in valid_coins:
    count += k // coin
    k = k % coin
    
    #coins_used.append(coin)
    if k == 0:
        break

print(count)
#print(coins_used)

'''
문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

예제 입력 1 
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
예제 출력 1 
6
예제 입력 2 
10 4790
1
5
10
50
100
500
1000
5000
10000
50000
예제 출력 2 
12
'''
