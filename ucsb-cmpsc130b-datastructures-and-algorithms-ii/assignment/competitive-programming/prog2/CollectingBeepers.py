'''
https://open.kattis.com/problems/beepers
'''

import sys

# iteration
def dfs_iter(cur_x, cur_y):
    global tmp, b, coordinates, visit, summation, count
    
    if summation > tmp:
        return 0
    if count == b:
        d = summation + abs(cur_x-pos[0])+abs(cur_y-pos[1])
        if d < tmp:
            tmp = d
        return 0
    
    for i in range(b):
        if visit[i] == 0:
            dist = abs(coordinates[i][0]-cur_x)+abs(coordinates[i][1]-cur_y);
            visit[i] = 1
            count += 1
            summation += dist
            dfs_iter(coordinates[i][0], coordinates[i][1])
            count -= 1
            summation -= dist
            visit[i] = 0
   

if __name__ == '__main__':
    # read the first line -- number of scenarios
    scenario = int(sys.stdin.readline())
    # empty list to store results to be printed
    res = []

    for _ in range(scenario):
        # size of the world
        x_size, y_size = [int(r) for r in sys.stdin.readline().split()]
        # starting position of Karel
        pos = [int(r) for r in sys.stdin.readline().split()]
        # number of beepers
        b = int(sys.stdin.readline())
        # coordinates of each beeper
        coordinates = []
        for beeper in range(b):
            coordinates.append([int(r) for r in sys.stdin.readline().split()])
        tmp = 9999999
        visit = [0 for _ in range(b)]
        summation = 0
        count = 0
        dfs_iter(pos[0], pos[1])
        print(tmp)
