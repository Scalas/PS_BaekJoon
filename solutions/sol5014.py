import sys

input = sys.stdin.readline
INF = float('inf')


# 5014 스타트링크
# 1층 부터 f층까지 있는 건물에서 위로 u층, 아래로 d층으로 가는 두 개의 버튼이 있는
# 엘레베이터를 타고 s층에서 시작하여 g층으로 가려할 때 버튼을 눌러야할 최소 횟수를 구하는 문제
def sol5014():
    f, s, g, u, d = map(int, input().split())

    # 이미 목적층에 있는 경우
    if s == g:
        return 0

    # 해당 층에 이미 방문했는지 체크
    visited = [False] * (f+1)
    
    # bfs로 버튼을 answer회 누를때마다 방문 가능한 층들을 검사
    # g층에 도달한다면 즉각 answer를 반환
    q = [s]
    visited[s] = True
    answer = 0
    while q:
        answer += 1
        nq = []
        for cur in q:
            # 아래로 이동
            nxt = cur-d
            if nxt == g:
                return answer
            if nxt > 0 and not visited[nxt]:
                visited[nxt] = True
                nq.append(nxt)

            # 위로 이동
            nxt = cur + u
            if nxt == g:
                return answer
            if nxt <= f and not visited[nxt]:
                visited[nxt] = True
                nq.append(nxt)
        q = nq

    # 방문 가능한 모든 층을 방문하고도 return되지 않았다면 g층엔 도달할 수 없음
    return 'use the stairs'
