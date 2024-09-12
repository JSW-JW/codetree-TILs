import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
starts = []
for _ in range(k):
    r, c = map(int, input().split())
    starts.append((r-1, c-1))
v = [[0 for _ in range(n)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = 0


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def is_wall(r, c):
    return g[r][c] == 1

def bfs(r, c):
    global ans
    q = deque([])
    q.append((r, c))
    v[r][c] = 1
    ans += 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not in_range(ny, nx) or is_wall(ny, nx):
                continue
            if v[ny][nx]:
                continue
            ans += 1
            v[ny][nx] = 1
            q.append((ny, nx))

"""
0 0 0
0 0 1
1 0 0
"""

for r,c in starts:
    if v[r][c]:
        continue
    bfs(r, c)

print(ans)