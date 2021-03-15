#0308_01_2869.py
'''
달팽이는 올라가고 싶다

문제
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

출력
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

예제 입력 1 
2 1 5
예제 출력 1 
4
예제 입력 2 
5 1 6
예제 출력 2 
2
예제 입력 3 
100 99 1000000000
예제 출력 3 
999999901
'''
'''
input_string = input().split()    #input_string 정수형 string
#print(input_string)
#print(type(input_string))
input_int = []
for each in input_string:
    each = int(each)
    input_int.append(each)

#print(input_int[0])
#print(type(input_int[0]))

#위의 과정을 좀 더 단순화 할 수 있는 방법(입력값 한 줄을 전부 정수화하여 어레이로 저장) 물어보기

up = input_int[0]
down = input_int[1]
height = input_int[2]

position = 0
day = 1
'''
'''
while True:
    position = position + up
    if position >= height:
        break
    position = position - down
    day = day+1
print(day)
'''
'''
while True:
    position = position + up
    if position < height:
        position = position - down
        day = day+1
    else:
        break
    
print(day)
'''


'''
#거꾸로 생각해보기(감산해나가기)
while (height-up > 0):
    day = day + 1
    height = height - (up - down)
print(day)
'''
'''
while (height-up > 0):
    day = day + 1
    height = height - (up - down)
print(day)
'''
#차이만큼 나눴을 때의 몫과 나머지
#만약에 나머지....
import math
up, down, height = input().split()
up = int(up)
down = int(down)
height = int(height)

time = math.ceil((height-up) / (up-down)) + 1
print(time)
'''
if (height % (up-down)) + down < up:   #마지막날이 불필요했던 경우
    print('그냥그날')
    time = height//(up-down)
    #if height % (up-down) + down < down : 
        #time = height//(up-down) - 1
elif (height % (up-down)) + down == up:   #마지막날이 필요했던 경우
    print('더하기1일')
    time = height//(up-down) +1
print(time)
'''
    

