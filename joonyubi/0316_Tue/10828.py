#0315_03_10828.py
#스택


import sys
r = sys.stdin.readline

n = int(r())

stack = []
result = []
for _ in range(n):
    string = r().strip()
    if string == 'pop':
        if len(stack) == 0:
            result.append('-1')
            continue
        popped = stack.pop()
        result.append(popped)
    elif string == 'size':
        result.append(len(stack))
    elif string == 'empty':
        if len(stack) == 0:
            result.append('1')
        else:
            result.append('0')
    elif string == 'top':
        if len(stack) == 0:
            result.append('-1')
            continue
        top = stack[-1]
        result.append(top)
    elif 'push' in string:   #command : push인 경우
        command, num = map(str, string.split())
        stack.append(int(num))

for i in result:
    print(i)
    

        

'''
스택 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	256 MB	95057	36320	26272	38.887%

문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 
문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1 
14
push 1  ->
push 2  ->
top     -> 2
size    -> 2
empty   -> 0
pop     -> 2
pop     -> 1
pop     -> -1
size    -> 0
empty   -> 1
pop     -> -1
push 3  -> 
empty   -> 0
top     -> 3

예제 입력 2 
7
pop     -> -1
top     -> -1
push 123
top
pop
top
pop
예제 출력 2 
-1
-1
123
123
-1
-1
'''
