#0315_04_2609.py
#최대공약수와 최소공배수

import sys
a, b = map(int, sys.stdin.readline().split())

'''
#testcase1
a, b = 24, 18
'''

def gcd(x,y):
    while True:
        if x == y:
            return x
        else:
            diff = abs(x-y)
            if x % diff == 0 and y % diff == 0:
                return diff
            else:
                if x<y:
                    y = y-x
                else:
                    x = x-y

def lcm(x,y):
    return x*y//gcd(x,y)

print(gcd(a, b))
print(lcm(a, b))
'''
if a==b:
    lcm = gcd
else:
    lcm = a*b//gcd
'''
#print(lcm)

'''
최대공약수와 최소공배수 출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	36156	21553	17702	62.769%
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

예제 입력 1 
24 18
예제 출력 1 
6
72
'''