import sys
n = int(sys.stdin.readline())
num_pairs = int(sys.stdin.readline())

graph = [[]for i in range(n+1)]     #그래프를 만드는 개념(각 n요소마다 dict로 연결컴퓨터 리스트 표시)
visited = []

for i in range(num_pairs):
    a, b = map(int, sys.stdin.readline().split())   #입력받을때마다 그래프의 해당 key값에 append(교차해서도 넣어주기)
    graph[a].append(b)
    graph[b].append(a)

print(graph)

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
[[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
'''