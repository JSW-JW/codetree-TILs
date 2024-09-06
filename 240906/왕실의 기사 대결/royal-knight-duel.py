import sys
input = sys.stdin.readline

L,N,Q = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(L)]
knights = []
for _ in range(N):
    r,c,h,w,k = map(int, input().split())
    knights.append([r-1,c-1,h,w,k])
cmds = [list(map(int, input().split())) for _ in range(Q)]

# idx 4 는 제자리를 의미
dr = [-1, 0, 1, 0, 0]
dc = [0, 1, 0, -1, 0]

executed = []

walls = set([(i, j) for i in range(L) for j in range(L) if g[i][j] == 2])

def in_range(idx, d):
    """
    :param idx: 기사의 순번
    :param d: 이동할 방향
    :return: True | False
    """
    r, c = knights[idx][0], knights[idx][1]
    nr, nc = r + dr[d], c + dc[d]
    return 0 <= nr < L and 0 <= nc < L

def get_area(idx, d):
    """
    :param idx: 기사의 순번
    :param d: 이동할 방향 (4: 제자리에서의 영역을 구하기 위함)
    :return: 이동 후 기사의 영역
    """
    r, c, h, w = knights[idx][0], knights[idx][1], knights[idx][2], knights[idx][3]
    nr, nc = r + dr[d], c + dc[d]
    area = [(nr + i, nc + j) for i in range(h) for j in range(w)]
    return area

def should_go(idx, d):
    """
    :param idx: 이동할 기사의 순번
    :param d: 이동할 방향
    :return: 벽에 막히거나 장외인지 여부  True | False
    """
    # 장외 체크
    if not in_range(idx, d):
        return False

    area = get_area(idx, d)
    # 벽에 막힘여부 체크
    for pos in area:
        if pos in walls:
            return False

    res = True
    for pos in area:
        for i, knight in enumerate(knights):
            if i == idx:
                continue
            # 각 기사의 현재 위치에 대한 영역
            another_area = get_area(i, 4)
            if pos not in another_area:
                continue
            # 충돌하는 기사에 대해서 재귀적으로 체크
            if i in executed:
                continue

            executed.append(i)
            sub_res = should_go(i, d)
            # 한 명이라도 진행할 수 없다면 모든 기사가 이동할 수 없음
            if sub_res == False:
                return False

    return res

for cmd in cmds:
    idx, d = cmd
    # 벽에 막혀서 이동할 수 없는지 여부 체크까지 완료
    executed = []
    print(should_go(idx-1, d))

"""
4 3 3
0 0 1 0
0 0 1 0
1 1 0 1
0 0 2 0
1 2 2 1 5
2 1 2 1 1
3 2 1 2 3
1 2
2 1
3 3
"""