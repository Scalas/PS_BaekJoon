import sys

input = sys.stdin.readline


# 1987 알파벳
# 격자형 지도에 각각 알파벳이 적혀있고 (0, 0)칸에서 시작한 말은 지금까지 지나온 칸들에
# 없었던 알파벳이 쓰인 칸으로만 갈 수 있을 때 말이 갈 수 있는 칸 수의 최댓값을 구하는 문제
# dfs 를 사용해도 풀 수 있지만 bfs 를 사용하는 방법이 더 간단하고 빠르다
def sol1987():
    R, C = map(int, input().split())
    # 비트마스크 사용을 위해 각 칸의 [A-Z] 의 알파벳을 1<<[0-25] 로 저장한다.
    board = [[1 << (ord(c) - ord('A')) for c in input().rstrip()] for _ in range(R)]

    # 시작위치느 (0, 0) 이며 아직까지 지나간 알파벳은 board[0][0] 뿐이다.
    q = {(0, 0, board[0][0])}

    # bfs 로 탐색 시작
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = 0
    while q:
        # 현재 방문칸수 1 증가
        answer += 1
        nq = set()
        for r, c, passed in q:
            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                # 비트연산으로 인접한 칸이 아직 지나간적 없는 알파벳인지 검사하고 지나간적이 없다면 큐에 삽입
                # 이전 칸들에 대한 방문여부 검사도 이 검사로 자동으로 해결된다
                # 같은칸, 같은 알파벳 방문상태는 큐가 set 이기 때문에 무시된다.(방문 상태가 같으려면 방문칸수가
                # 같을 수 밖에 없기 때문에 set 만으로 모두 걸러낼 수 있다.)
                if 0 <= nr < R and 0 <= nc < C and not passed & board[nr][nc]:
                    nq.add((nr, nc, passed | board[nr][nc]))
        q = nq

    return answer
