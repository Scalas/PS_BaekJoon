import sys

input = sys.stdin.readline


# 1 ~ n 번의 승객이 공항에서 오름차순으로 줄을서서 여권심사를 받아 출구로 빠져나가려 하고
# 공항에 여권 심사창구가 k개 있으며 각 여권 심사대에는 번호가 빠른 사람이 먼저 들어갈 수 있으며
# 여러개의 여권 심사창구중 어느곳을 고를지는 승객의 자유이고
# 심사를 끝내고 나올 때 같은 심사대에 줄선 사람들은 줄선 순서대로 나오지만 다른 심사대끼리는 순서가 없다
# 이 때, 승객의 수 n과 여권 심사창구의 수 k, 승객들이 나갈떄의 순서가 리스트로 주어졌을 때
# 나갈떄의 순서 리스트가 실제로 가능한지 구하는 문제
def sol16288():
    n, k = map(int, input().split())
    passenger = list(map(int, input().split()))
    
    # 승객들이 같은 큐에 들어가려고 할 떄는 반드시 줄선 순서대로 들어가야하므로
    # 같은 큐의 승객들은 오름차순으로 정렬되어있음
    # 겹치지 않게 증가하는 부분 수열의 갯수를 구하면 필요한 큐(여권 심사 창구)의 갯수를 구할 수 있음
    visited = [False] * n
    count = 0
    for i in range(n):
        # 아직 심사 창구에 들어가지 못한 승객이 남아있을 경우
        if visited[i]:
            continue
        visited[i] = True

        # 여권 심사창구가 k를 넘어서면 NO를 반환
        count += 1
        if count > k:
            return 'NO'

        # 아직 심사 창구에 들어가지 못한 승객들을 대상으로 증가하는 부분수열 탐색
        pre = passenger[i]
        for j in range(i + 1, n):
            if visited[j]:
                continue
            cur = passenger[j]
            if cur > pre:
                pre = cur
                visited[j] = True
    
    # 모든 승객들이 심사창구에 들어가고도 심사창구의 수가 모자라지 않는다면 YES 반환
    return 'YES'
