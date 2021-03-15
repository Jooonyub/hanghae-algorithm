#0315_03_1037.py
#약수

import sys
num_divisor = int(sys.stdin.readline())
divisors = list(map(int,sys.stdin.readline().split()))

def toSigned32(n):
    n = n & 0xffffffff
    return n | (-(n & 0x80000000))

divisors.sort()

N = divisors[0]*divisors[-1]

#print(type(toSigned32(N)))
print(toSigned32(N))

#N max() * min()의 방법이 훨씬 간결

'''
#testcase1
num_divisor = 2
divisors = [4,2]
#N-> 8
'''
'''
#testcase2
num_divisor = 3
divisors = [8,4,2]
#N -> 16
'''
'''
#testcase3
num_divisor = 4
divisors = [6,2,4,3]
#N -> 12
'''


'''

4 -> 2
6 -> 2,3
8 -> 2,4
9 -> 3
10 -> 2,5
12 -> 2,3,4,6
'''

'''
약수 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	23425	11424	10015	49.779%
문제
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 
둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

출력
첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.

예제 입력 1 
2
4 2
예제 출력 1 
8

'''