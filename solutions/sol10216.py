import sys

input = sys.stdin.readline


# 10216 Count Circle Groups
# 테스트케이스별로 n개의 진영의 좌표와 반지름이 주어졌을 때 영역이 겹치는 진영은 하나의 진영이 된다
# 각 테스트케이스의 진영의 총 갯수를 구하는 문제
def sol10216():
    answers = []
    for _ in range(int(input())):
        n = int(input())

        # 두 진영 사이의 거리가 반지름의 합 이하인 경우 간선을 생성
        g = [[] for _ in range(n)]
        pos = [list(map(int, input().split()))]
        for i in range(1, n):
            x, y, r = map(int, input().split())
            for j in range(len(pos)):
                px, py, pr = pos[j]
                if ((px - x) ** 2 + (py - y) ** 2) <= (r + pr) ** 2:
                    g[i].append(j)
                    g[j].append(i)
            pos.append([x, y, r])

        # bfs로 분리된 집합 갯수 구하기
        visited = [False] * n
        answer = 0
        for i in range(n):
            if not visited[i]:
                answer += 1
                q = [i]
                while q:
                    nq = []
                    for cur in q:
                        for nxt in g[cur]:
                            if not visited[nxt]:
                                visited[nxt] = True
                                nq.append(nxt)
                    q = nq
        answers.append(answer)

    return '\n'.join(map(str, answers))
