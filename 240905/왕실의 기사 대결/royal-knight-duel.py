import sys
input = sys.stdin.readline

L,N,Q = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(L)]
knights = [list(map(int, input().split())) for _ in range(N)]
cmds = [list(map(int, input().split())) for _ in range(Q)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

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
    print(idx, d)
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
            another_area = get_area(i, d)
            if pos not in another_area:
                continue
            # 충돌하는 기사에 대해서 재귀적으로 체크
            sub_res = should_go(i, d)
            print(f'sub_res = {sub_res}')
            # 한 명이라도 진행할 수 없다면 모든 기사가 이동할 수 없음
            if sub_res == False:
                return False

    return res

for cmd in cmds:
    idx, d = cmd
    print(should_go(idx-1, d))
"""
4 3 1
0 0 1 0
0 0 1 0
1 1 0 1
0 0 2 0
1 2 2 1 5
2 1 2 1 1
3 2 1 2 3
1 2
"""