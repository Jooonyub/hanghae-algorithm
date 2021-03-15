#0309_02_11651.py
#title: 좌표 정렬하기

'''
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

예제 입력 1 
5
0 4
1 2
1 -1
2 2
3 3
예제 출력 1 
1 -1
1 2
2 2
3 3
0 4
'''
N = int(input())    #N : 평면 위의 점 개수

points = list(range(N))

y_list = list()

for i in range(N):
    x, y = map(int, input().split())
    points[i] = [x,y]
    y_list.append(y)

def extractX(point):
  return point[0]

def extractY(point):
  return point[1]

points.sort(key=extractY)
ordered_points = []
y_list.sort()

cnt = 0
while cnt < len(points):
    num_y = y_list.count(points[cnt][1])
    if num_y == 1:
        ordered_points.append(points[cnt])    
    else:
        same_y = points[cnt: cnt + num_y + 1]
        same_y.sort(key=extractX)
        ordered_points.extend(same_y)
    cnt = cnt + num_y

for point in ordered_points:
    print(point)


















'''
N = int(input())    #N : 평면 위의 점 개수

points = list(range(N))
#print(N)

y_set = set()    #or {}
y_list = list()

for i in range(N):
    x, y = map(int, input().split())
    points[i] = [x,y]
    y_set.add(y)
    y_list.append(y)

for point in points:
    print(point)

def extractX(point):
  return point[0]

def extractY(point):
  return point[1]

points.sort(key=extractY)
ordered_points = []
y_list.sort()
#same_y=[]

for point in points:
    print(point)

cnt = 0
while cnt < len(points):
    num_y = y_list.count(points[cnt][1])
    if num_y == 1:
        ordered_points.append(points[cnt])    
    else:
        same_y = points[cnt: cnt + num_y + 1]
        same_y.sort(key=extractX)
        ordered_points.extend(same_y)
    cnt = cnt + num_y

for point in ordered_points:
    print(point)
'''
'''
for i in len(points):
    num_y = y_list.count(point[1])
    if num_y == 1:
        ordered_points.append(point)
    else:
'''  

'''
N = int(input())    #N : 평면 위의 점 개수

points = list(range(N))
#print(N)

for i in range(N):
    x, y = map(int, input().split())
    points[i] = [x,y]

for point in points:
    print(point, type(point), type(point[0]))

ordered_points = []
'''
'''
for i in range(N):
    for j in list(range(0,i))+list(range(i+1,N)):
        if points[i][1] > points[j][1]: #더 작은 y값이 나올때
            points[i] = points[j] #교체
        elif points[i][1] == points[j][1]:  #y값 크기가 같을 때
            if points[i][0] > points[i][0]: #더 작은 x값이 나올때
                points[i] = points[j] #교체
        ordered_points.append(points[i])
        #points.pop(points[i])
'''
'''
ylist = []
for i in range(N):
    ylist.append(points[i][1])
ylist.sort()
print(ylist)

for i in points:
    if ylist.count(ylist[i]) != 1:
        #x값 비교
        xlist = []
        for j in range(ylist.count(ylist[i])):





for point in ordered_points:
    print(point)
'''