import sys

input = sys.stdin.readline
sys.setrecursionlimit(10001)


# 2250 트리의 높이와 너비
# 노드가 n개인 이진탐색트리의 각 노드의 자식노드 정보가 주어졌을 때
# 격자공간상에 트리의 노드들을 열이 겹치지않게 그렸을 경우
# 각 레벨의 가장 우측의 노드의 열번호에서 가장 좌측의 열번호를 빼고 1을 더한 값을 해당 레벨의 너비라고 한다
# 각 레벨중 가장 너비가 큰 레벨과 그 너비를 구하는 문제
# 단, 같은 너비라면 레벨이 더 낮은(작은) 쪽을 우선시한다.
def sol2250():
    n = int(input())
    g = [[] for _ in range(n+1)]
    d = [0] * (n+2)
    for _ in range(n):
        u, v, w = map(int, input().split())
        g[u].append(v)
        g[u].append(w)
        d[v] += 1
        d[w] += 1

    # 각 레벨의 최소, 최대위치
    lev_bound = dict()

    # 열번호
    idx = 1

    def dfs(cur, level):
        nonlocal idx

        # NIL
        if cur < 0:
            return

        # 좌측 자식노드 탐색
        dfs(g[cur][0], level+1)

        # 현재 노드의 열번호로 현재 레벨의 최소, 최댓값 갱신
        if level not in lev_bound:
            lev_bound[level] = [idx, idx]
        else:
            lev_bound[level][0] = min(lev_bound[level][0], idx)
            lev_bound[level][1] = max(lev_bound[level][1], idx)

        # 열번호 1 증가
        idx += 1

        # 우측 자식노드 탐색
        dfs(g[cur][1], level+1)

    # 루트노드 탐색
    root = 1
    while d[root]:
        root += 1

    # 루트노드로부터 이진탐색트리의 in-order 순회 시작
    dfs(root, 1)

    # 각 레벨중 너비가 최솟값인 레벨과 그 너비를 탐색
    # 같은 너비라면 레벨이 더 낮은쪽을 저장
    lv, width = 0, 0
    for level, bound in lev_bound.items():
        wd = bound[1] - bound[0] + 1
        if wd > width:
            lv, width = level, wd
        elif wd == width and level < lv:
            lv = level

    return ' '.join(map(str, [lv, width]))
