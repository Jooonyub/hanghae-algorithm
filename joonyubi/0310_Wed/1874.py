#0310_02_1874.py
#스택수열

stack = list()
plus_minus = list()
n = int(input())
count = 1
isAvailable = True

for i in range(n):
    num = int(input())

    while count <= num:     #count가 입력받는 수와 같아질때까지 push
        stack.append(count)
        plus_minus.append('+')
        count += 1

    if stack[-1] == num:        #스택의 맨 마지막 값과 입력받는 수가 같다면 pop 처리
        stack.pop()
        plus_minus.append('-')
    else:                       #스택의 맨 마지막 값과 입력받는 수가 다르다면 'No'
        isAvailable = False

if isAvailable == False:
    print('NO')
else:
    for j in plus_minus:
        print(j)

    

    
'''
# 스택의 최상단에 수를 하나 더 쌓습니다
def stack_push():
    global stack, stack_sign_list, push_index

    stack.append(push_index + 1)
    stack_sign_list.append("+")
    push_index += 1

# 스택 최상단의 요소를 빼냅니다
def stack_pop():
    global stack, stack_sign_list

    popped = stack.pop()
    stack_sign_list.append("-")
    return popped

input_count = int(input())    #n개의 수

input_number = int(input())

for i in range(input_number):
    stack_push()

stack_pop()

for i in range(input_count-1):
    input_number = int(input())

    if len(stack) == 0:
        stack_push()

    # 입력한 숫자에 다다를 때까지 stack을 하나 쌓습니다
    while stack[len(stack) - 1] < input_number:
        stack_push()

    # Error
    # 스택의 최상단의 수가 입력받은 수에 도달할 만큼 쌓아봤지만
    # 스택에 쌓인 최상위 수와 일치하지 않다면 표현이 불가능한 식입니다
    if stack[len(stack) - 1] > input_number or stack[len(stack) - 1] < input_number:
        print("NO")
        stack_sign_list.clear()
        break

    # 입력한 숫자와 stack의 가장 최상위 숫자가 일치할 때 pop합니다
    stack_pop()

# 스택에 push 또는 pop한 기록을 출력합니다
for sign in stack_sign_list:
    print(sign)
'''  






'''
문제
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
이를 계산하는 프로그램을 작성하라.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

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