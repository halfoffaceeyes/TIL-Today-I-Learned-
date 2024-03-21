# 최소 비용 신장 트리(MST)
* 그래프에서 최소 비용 문제
  * 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
  * 두 정점 사이의 최소 비용의 경로 찾기
* 신장 트리
  * n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리
* 최소 신장 트리(Minimum Spanning Tree)
  * 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

* Prim과 Kruskal 알고리즘은 모두 Greedy
## Prim 알고리즘
* 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
  1) 임의 정점을 하나 선택해서 시작
  2) 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택 = BFS와 유사하므로 queue에 우선순위를 부여해서 구현
  3) 모든 정점이 선택될 때까지 1),2)과정을 반복
* 서로소인 2개의 집합(2 disjoint-sets 정보를 유지)
  * 트리 정점들(tree vertices) - MST를 만드리 위해 선택된 정점들
  * 비트리 정점들(nontree vertices) - 선택되지 않은 정점들

![prim 알고리즘 적용예시1](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240321/prim%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98.PNG)
![prim 알고리즘 적용예시2](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240321/prim%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%982.PNG)

```py
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# 우선 순위 큐 활용
from heapq import heappush,heappop

def prim(start):
    pq=[]
    MST=[0]*V
    sum_weight=0
    # 시작점 추가
    # [기존 BFS] 노드 번호만 관리
    # [PRIM] 가중치가 낮으면 먼저 나와야한다.
    # -> 관리해야할 데이터 : 가중치, 노드 번호 2가지
    # -> 동시에 두가지 데이터 다루기
    #       1. class 로 만들기 (3가지 이상의 데이터는 꼭 클래스로 연습할것)
    #       2. 튜플로 관리
    heappush(pq,(0,start))

    while pq:
        weight, now = heappop(pq)
        if MST[now]: # 우선순위 큐이므로 bfs를 진행하는 과정에서 동일한 노드가 같이 저장되는 경우가 있음. 그래서 더짧은 거리를 먼저 탐색하는 과정이 진행되므로 짧은 거리에서 방문 여부를 확인할 필요가 있음
            continue
        # 방문처리
        MST[now]=1
        # 누적합 추가
        sum_weight += weight
        #갈 수 있는 노드들을 보면서
        for i in range(V):
            # 갈 수 없다면 pass
            if graph[now][to]==0 or MST[to]:
                continue
            heappush(pq,(graph[now][to],to))
    print(f'최소비용 : {sum_weight}')

V,E = map(int,input().split())
# 인접행렬로 저장
# 인접리스트로 저장
graph = [[0]*V for _ in range(V)]
for _ in range(E):
    s,e,w = map(int,input().split())
    # 기존 그래프 3->4 로 갈 수 있다.
    # graph[3][4]=1

    # 가중치 그래프 3->4로 가는데 31이라는 비용이든다.
    # graph[3][4]=31
    graph[s][e]=w
    graph[e][s]=w

```
![prim 알고리즘 수도코드](<../이미지/240321/prim알고리즘 수도.PNG>)

## Kruskal 알고리즘
* 간선을 하나씩 선택해서 MST를 찾는 알고리즘
  1) 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
  2) 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
    - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
  3) n-1개의 간선이 선택될때 까지 2)를 반복

```py
# 1. 전체 그래프를 보고, 가중치가 제일 작은 간선부터 뽑자
#   -> 코드로 구현: 전테 간선 정보를 저장 + 가중치로 정렬

# 2. 방문 처리
#   -> 이 때, 싸이클이 발생하면 안된다!
#   -> 싸이클 여부?? union-find 알고리즘을 활용

def find_set(x):
    if parents[x]==x:
        return x
    # 경로 압축
    parents[x]=find_set(parents[x])
    return parents[x]

def union(x,y):
    x=find_set(x)
    y=find_set(y)
    
    # 같은 집합이면 pass
    if x==y:
        return
    if x<y:
        parents[y]=x
    else:
        parents[x]=y

V,E= map(int,input().split())
edges=[] # 간선 정보들을 모두 저장

for _ in range(E):
    s,e,w = map(int,input().split())
    edges.append([s,e,w])

edges.sort(key=lambda x : x[2])
parents = [i for i in range(V)] # 대표자 배열(Union-find를 위한)
sum_weight=0
cnt=0
# 간선들을 모두 확인한다.
for s,e,w in edges:
    # 싸이클이 발생하면 pass
    # -> 이미 같은 집합에 속해 있다면 pass
    if find_set(s)==find_set(e):
        print(s,e,w,'/싸이클 발생! 탈락!')
        continue  
    # 싸이클이 없으면, 방문 처리
    print(s,e,w)
    cnt+=1
    union(s,e)
    sum_weight+=w
    if cnt==V-1: # MST 완성시점 == 간선의 개수 v-1개 일때
        break

print(f'최소비용 ={sum_weight}')
```

![Kruskal 알고리즘1](<../이미지/240321/Kruskal 알고리즘1.PNG>)

![Kruskal 알고리즘2](<../이미지/240321/Kruskal 알고리즘2.PNG>)

![Kruskal 알고리즘3](<../이미지/240321/Kruskal 알고리즘3.PNG>)

![Kruskcal 알고리즘 수도](<../이미지/240321/Kruskal 알고리즘 수도.PNG>)

# 최단 경로(Dijkstra)
* 최단 경로 정의
  * 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
* 하나의 시작 정점에서 끝 정점까지의 최단 경로
  * 다익스트라(dijkstra)알고리즘
    * 음의 가중치를 허용하지 않음
  * 벨만-포드(Bellman-Ford) 알고리즘
    * 음의 가중치 허용
* 모든 정점들에 대한 최단 경로
  * 플로이드-워샬(Floyd-Warshall) 알고리즘
  
## Dikstra 알고리즘
* 시작 정점에서 누적 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하느 방식
* 시작정점(s)에서 끝정점(t)까지의 최단 경로에 정점 x가 존재
* 이 때, 최단 경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단 경로로 구성
* 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사

## 다익스타라 알고리즘 적용 예시
![Dijkstra 수도 코드](<../이미지/240321/Dijkstra 수도 코드.PNG>)

![Dijkstra 알고리즘1](<../이미지/240321/Dijkstra 알고리즘 1.PNG>)

![Dijkstra 알고리즘2](<../이미지/240321/Dijkstra 알고리즘 2.PNG>)

![Dijkstra 알고리즘3](<../이미지/240321/Dijkstra 알고리즘 3.PNG>)

![Dijkstra 알고리즘4](<../이미지/240321/Dijkstra 알고리즘 4.PNG>)

![Dijkstra 알고리즘5](<../이미지/240321/Dijkstra 알고리즘 5.PNG>)

![Dijkstra 알고리즘6](<../이미지/240321/Dijkstra 알고리즘 6.PNG>)

![Dijkstra 알고리즘7](<../이미지/240321/Dijkstra 알고리즘 7.PNG>)

![Dijkstra 알고리즘8](<../이미지/240321/Dijkstra 알고리즘 8.PNG>)

![Dijkstra 알고리즘9](<../이미지/240321/Dijkstra 알고리즘 9.PNG>)

```py
from heapq import heappush,heappop

INF = int(1e9)

V,E = map(int,input().split())
start =0 # 시작 노드 번호
#인접리스트
graph =[[] for_ in range(V)]
# 누적 거리를 저장할 변수
distance = [INF] * V

#간선 정보 저장
for _ in range(E):
    s,e,w = map(int,input().split())
    graph[s].append([w,e])

def dijkstra(start):
    pq=[]
    # 시작점의 weight, node 번호를 한번에 저장
    heappush(pq,(0,start))
    # 시작 노드 초기화
    distance[start]=0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)
        
        # now 가 이미 처리된 노드라면 pass
        if distance[now] <dist:
            continue
        # pq의 특성 때문에 더 긴거리가 미리 저장되어 있음
        # now에서 인접한 다른 노드 확인
        for to in graph[now]:
            new_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist+next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            distance[next_node]= new_dist # 누적거리를 최단 거리로 갱신
            heappush(pq,(new_dist,next_node)) # next_node의 인접 노드들을 pq에 추가
dijkstra(0)
print(distance)
```

