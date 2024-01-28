import sys
from collections import deque

def main() : 
    y, x = map(int, input().split())

    # make maze
    maze = []
    maze.append([0 for i in range(x + 2)])
    for _ in range(y) :
        maze.append([0] + list(map(int, list(input()))) + [0])
    maze.append([0 for i in range(x + 2)])

    print(findPath(maze, (y, x)))

def findPath(maze, target) :
    y, x = target
    timeTable = [[10001 for _ in range(x + 2)] for i in range(y + 2)]
    timeTable[1][1] = 1
    now = (1, 1)
    frontier = deque()
    while(1) :
        makeFrontier(maze, timeTable, now, frontier)
        now = frontier.popleft()

        # get to target
        if(now == (x, y)) : return timeTable[y][x]

def makeFrontier(maze, timeTable, now, frontier) :
    x, y = now
    time = timeTable[y][x]

    for x2, y2 in [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)] :
        if(maze[y2][x2] and time + 1 < timeTable[y2][x2]) : 
            frontier.append((x2, y2))
            timeTable[y2][x2] = time + 1

main()