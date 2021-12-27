import sys

input = sys.stdin.readline
INF = 10 ** 9
n = int(input())


# 2666 벽장문의 이동
# n개의 같은크기의 벽장이 나란히 서있고 그중 두개의 문이 비어있으며
# 문들은 인접한 벽장의 문이 비어있을 경우 그쪽으로 이동 가능하다.
# 벽장의 갯수 n과 문이 비어있는 두 개의 벽장의 위치,
# 문을 치우고 사용해야할 벽장의 수와 그 순서가 주어졌을 때
# 문의 이동횟수의 최솟값을 구하는 문제
def sol2666():
    o1, o2 = map(int, input().split())
    k = int(input())
    cmd = list(map(lambda x: int(x)-1, [input() for _ in range(k)]))

    # 벽장문의 초기 상태를 비트마스크로 표현
    init_state = (1 << n) - 1 - (1 << (o1-1)) - (1 << (o2-1))

    # dp[k][state] 는 벽장문의 상태가 state 이고 cmd[k] 번째 벽장을 사용해야할 때
    # 남은 사용해야할 벽장을 모두 사용하기 위해 필요한 최소 이동횟수
    dp = [dict() for _ in range(k)]

    def dfs(state, cur):
        # 사용해야할 벽장을 모두 사용했을 경우 더이상의 이동은 필요없음
        if cur == k:
            return 0

        # 벽장의 상태가 state 이고 cmd[cur] 번째 벽장을 사용해야할 때
        # 남은 사용해야할 벽장을 모두 사용하기 위해 필요한 최소 이동횟수가 아직 계산되지 않은 경우
        if not dp[cur].get(state):
            res = INF
            # 오른쪽으로 벽장을 밀 수 있다면 밀어본다
            rnxt_state, rcnt = push(state, cmd[cur], 1)
            if rcnt >= 0:
                res = min(res, dfs(rnxt_state, cur+1) + rcnt)

            # 왼쪽으로 벽장을 밀 수 있다면 밀어본다
            lnxt_state, lcnt = push(state, cmd[cur], 0)
            if lcnt >= 0:
                res = min(res, dfs(lnxt_state, cur+1) + lcnt)

            # 오른쪽으로 민 경우와 왼쪽으로 민 경우중 총 이동횟수가 가장 적은것을 저장
            dp[cur][state] = res

        return dp[cur][state]

    # 초기상태이고 첫 번째로 사용해야할 벽장을 사용할 차례일 때의 남은 최소이동횟수 반환
    return dfs(init_state, 0)


# 벽장문을 왼쪽, 또는 오른쪽으로 밀어내는 함수
# 밀어낸 후의 상태, 필요한 이동횟수를 튜플로 반환
def push(state, idx, direction):
    pos = 1 << idx

    # 이미 해당 벽장이 비어있을 경우 상태는 그대로, 이동횟수는 0
    if not state & pos:
        return state, 0

    # 오른쪽으로 미는 경우
    if direction:
        for cnt in range(1, n-idx):
            pos <<= 1
            if not state & pos:
                return state + pos - (1 << idx), cnt

    # 왼쪽으로 미는 경우
    else:
        for cnt in range(1, idx+1):
            pos >>= 1
            if not state & pos:
                state -= pos
                return state, cnt
            state -= pos

    # 밀려는 방향으로 밀 수 없는 경우
    return -1, -1
