import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
relation = []
visited = []

def main() :
    global relation
    global visited
    numVertex, numEdge, startPoint = map(int, input().split())
    relation = [[] for i in range(numVertex + 1)]

    # make relation between vertices
    makeRelation(numEdge)

    # excute dfs
    visited = [True] + [False for i in range(numVertex)]
    dfs(startPoint)
    print()

    # excute bfs
    visited = [True] + [False for i in range(numVertex)]
    bfs(startPoint)

def makeRelation(numEdge) :
    for _ in range(numEdge) :
        vertexA, vertexB = map(int, input().split())
        relation[vertexA].append(vertexB)
        relation[vertexB].append(vertexA)
    for i in relation :
        i.sort()

def dfs(initial) :
    now = initial
    print(now, end = " ")
    visited[now] = True
    for i in relation[now] :
        if(not visited[i]) : dfs(i)
    
def bfs(initial) :
    now = initial
    frontier = deque()
    while(1) :
        visited[now] = True
        print(now, end = " ")
        for i in relation[now] :
            if(not visited[i] and i not in frontier) : frontier.append(i)

        # empty
        if(not frontier) : break
        now = frontier.popleft()

main()