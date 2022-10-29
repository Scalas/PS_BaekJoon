import sys

input = sys.stdin.readline


# 9205 맥주 마시면서 걸어가기
# 시작 위치 sr, sc 에서 도착지 er, ec 로 걸어갈 때
# 50미터 마다 맥주를 한 병 마셔야하고
# 맥주는 시작시 20병 가지고 시작하며 편의점에 들를 경우 20병이 채워진다고 할 때
# 도착지에 도착 가능한지 여부를 구하는 문제
def sol9205():
    
    # 50미터에 맥주 한 병이 필요하고 매 노드를 거칠 때마다 20병의 맥주를 채울 수 있기 때문에
    # 사실상 노드 사이의 거리가 최대 1000인 경우에만 연결되어있는 그래프라고 생각할 수 있음
    # 도착 가능 여부를 빠르게 판단하기 위해 bfs를 사용
    def bfs():
        nonlocal n, sr, sc, er, ec

        q = [(sr, sc)]
        visited = set()
        while q:
            nq = []
            for cr, cc in q:
                for nr, nc in nodes:
                    if abs(nr - cr) + abs(nc - cc) > 1000:
                        continue
                    if nr == er and nc == ec:
                        return 'happy'
                    key = (nr, nc)
                    if key in visited:
                        continue
                    visited.add(key)
                    nq.append(key)
            q = nq
        return 'sad'

    answer = []

    for _ in range(int(input())):
        n = int(input())
        sr, sc = map(int, input().split())
        nodes = [list(map(int, input().split())) for _ in range(n)]
        er, ec = map(int, input().split())
        nodes.append([er, ec])
        answer.append(bfs())

    return '\n'.join(answer)
