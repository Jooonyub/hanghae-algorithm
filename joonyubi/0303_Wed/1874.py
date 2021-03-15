#0310_02_1874.py
#스택 수열

'''
문제
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
이를 계산하는 프로그램을 작성하라.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 
둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 
물론 같은 정수가 두 번 나오는 일은 없다.

출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

예제 입력 1 
8
4
3
6
8
7
5
2
1
예제 출력 1 
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
예제 입력 2 
5
1
2
5
3
4
예제 출력 2 
NO
힌트
1부터 n까지에 수에 대해 차례로 [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.
'''
#import sys

#n = sys.stdin.readline()

n = int(input())
stacks = []
numbers = list(range(1,n+1))
for _ in range(n):
    stacks.append(int(input()))
#print(stacks, type(stacks), type(stacks[0]))    #정수형으로 잘 담겼는지 확인을 위한 출력문

'''
n = 8
stacks = [4,3,6,8,7,5,2,1]
numbers = [1,2,3,4,5,6,7,8]
'''
'''
실제의 수 : numbers[stacks[0]-1] or 
stacks[0].pop을 하면 그다음순서는 계속 stacks[0]
'''
#제외할때 '-' 표시
signbox = []
popped = []
idx_before = 0

for stack in stacks:    #for문을 통해 stacks의 하나하나 값을 보여주고
    idx = numbers.index(stack)  #해당 stack의 index를 numbers에서 찾는다.
    diff = idx - idx_before + 1
    if diff > 0:    #수열에서 수가 증가하는 경우
        signbox.extend(['+']*diff)
    elif diff < 0:  
        print("No")
        signbox.clear
        break
    signbox.append('-')
    idx_before = idx
    numbers.pop(idx)    #numbers list에서는 이 값을 빼주고
    #signbox.append('-')

for sign in signbox:
    print(sign)

'''
rightbefore = 0
for num in stack:
    stack.pop(num)
    popped.append(num)
    diff = num - rightbefore
    if diff > 0:    #위로 올라가는 경우
        signbox.extend(['+']*diff)
        signbox.append('-')
    else:   #
        signbox.extend
'''