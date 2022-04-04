import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, sys.stdin.readline().rstrip().split())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

one = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            one += 1

def meltdown(cnt):
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 1:
                    board[nx][ny] = 2
                    cnt -= 1
                else:
                    q.append((nx, ny))
    return cnt

def make_zero():
    for i1 in range(n):
        for i2 in range(m):
            if board[i1][i2] == 2:
                board[i1][i2] = 0

q = deque()
res = 0
tmp = one

while one != 0:
    visited = [[False] * m for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = True
    one = meltdown(one)

    if one != 0:
        tmp = one
    res += 1
    make_zero()

print(res)
print(tmp)
