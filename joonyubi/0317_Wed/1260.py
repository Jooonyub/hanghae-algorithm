#0316_0_.py
#DFS와 BFS 분류

import sys
r = sys.stdin.readline

n, m , v = map(int, r().split())
#n, m, v = 4, 5, 1

graph = dict()

for i in range(1,n+1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, r().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

#print(graph)

#나는 stack 구조로 접근했지만, 답안을 보니 재귀구조로 풀어야 했던 문제네..... 시댕.........
'''
def dfs_graph(adjacent_graph, start_node):
    stack = [start_node]
    dfs_visited = []
    
    while stack:
        current_node = stack.pop()
        if current_node not in dfs_visited:
            dfs_visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in dfs_visited:
                stack.append(adjacent_node)
    return dfs_visited
'''
visited = []
def dfs_recursion(adjacent_graph, current_node, visited_array):
    if current_node not in visited_array:
        visited_array.append(current_node)
    for adjacent_node in adjacent_graph[current_node]:
        if adjacent_node not in visited_array:
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)
    return visited_array


def bfs_queue(adjacent_graph, start_node):
    queue = [start_node]
    bfs_visited = []
    
    while queue:
        current_node = queue.pop(0)
        if current_node not in bfs_visited:
            bfs_visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in bfs_visited:
                queue.append(adjacent_node)
    return bfs_visited

dfs_result = dfs_recursion(graph, v, visited)
bfs_result = bfs_queue(graph, v)

dfs_sequence = ' '.join(map(str, dfs_recursion(graph, v, visited)))
bfs_sequence = ' '.join(map(str, bfs_queue(graph, v)))

print(dfs_sequence)
print(bfs_sequence)

#피드백
#첫째로 조인을 몰라서 헤맸고(list.join() _ string type에서만 유효하다.)
    #66-67
#둘째로 dfs의 방향에서 recursion으로 접근하는 답안이었으나 stack으로 접근해서 헤맸고
    #27-38 -> 40-47
#셋째로 입력받은 graph의 각 key별 value값들이 오름차순 정렬이 되어있지 않아 헤맸다.
    #20-21
'''
# list => string
time_list
['10', '34', '17']
':'.join(time_list)
'10:34:17'
'''

'''
DFS와 BFS 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	123388	43655	25147	33.607%
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
graph = {
    1: [2,3,4]
    2: [2,4]
    3: [1,4]
    4: [1,2,3]
}
예제 출력 1 
1 2 4 3
1 2 3 4
예제 입력 2 
5 5 3
5 4
5 2
1 2
3 4
3 1
graph = {
    1: [2,3]
    2: [1,5]
    3: [1,4]
    4: [3,5]
    5: [1,4]
}
예제 출력 2 
3 1 2 5 4
3 1 4 2 5
예제 입력 3 
1000 1 1000
999 1000
예제 출력 3 
1000 999
1000 999
'''