#0316_06_18258.py
#큐 2

import sys
from collections import deque
r = sys.stdin.readline

n = int(r())

queue = deque()

def Command(string):
    if string == 'pop':
        if len(queue) == 0:
            return -1
        return queue.popleft()
    elif string == 'size':
        return len(queue)
    elif string == 'empty':
        if len(queue) == 0:
            return 1
        else:
            return 0
    elif string == 'front':
        if len(queue) == 0:
            return -1
        else:
            return queue[0]
    elif string == 'back':
        if len(queue) == 0:
            return -1
        else:
            return queue[-1]
    else:
        queue.append(string.split()[1])
        return

results = []
for _ in range(n):
    phrase = r().strip()
    results.append(Command(phrase))

for result in results:
    if result == None:
        continue
    print(result)

'''
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
27324932	ckjy1105	18258	맞았습니다!!	163052	2152	Python 3 / 수정	867	1분 전
'''

#queue = []
'''
큐 2 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초 (하단 참고)	512 MB	18583	5608	4485	30.993%

문제
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 
문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1 
15
push 1      
push 2      
front       1
back        2
size        2
empty       0
pop         1
pop         2
pop         -1
size        0
empty       1
pop         -1
push 3      
empty       0
front       3
예제 출력 1 
1
2
2
0
1
2
-1
0
1
-1
0
3
'''