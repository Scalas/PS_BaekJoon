import sys

input = sys.stdin.readline
bit = [1 << i for i in range(10)]


# 1014 컨닝
# n * m의 공간에 한칸마다 자리가 있고 자리에는 한명의 학생이 앉을 수 있다.
# 학생은 왼쪽 위, 오른쪽 위, 왼쪽, 오른쪽을 컨닝할 수 있으며
# 몇개의 자리는 이미 부서져있어 앉을 수 없다.
# 학생들이 서로 컨닝하지 못하도록 앉히려 할 때 앉힐 수 있는 최대 학생 수를 구하는 문제
def sol1014():
    def dfs(r, pre_state):
        # 모든 행에 학생을 앉혔다면 더이상 앉힐 수 없음
        if r == n:
            return 0

        # 이미 계산된 경우가 아니라면
        if dp[r][pre_state] < 0:
            res = 0
            # 현재 행에서 학생을 앉힐 수 있는 모든 경우의 수
            for cur_state, bit_cnt in cand_bits:
                # 부서진 의자에 앉게되는 경우 패스
                if cur_state & broken[r]:
                    continue

                # 컨닝이 가능한 경우 패스
                if is_cheating_possible(pre_state, cur_state, m):
                    continue

                # 다음 행으로 넘어간다.
                res = max(res, dfs(r+1, cur_state) + bit_cnt)

            # 현재 r행의 자리에 학생을 앉힐 차례이며 이전 상태가 pre_state 일 때
            # 앞으로(r~n-1 행까지) 앉힐 수 있는 최대 학생 수
            dp[r][pre_state] = res

        return dp[r][pre_state]

    answer = []
    for _ in range(int(input())):
        n, m = map(int, input().split())

        # 망가진 의자의 정보를 비트마스크로 저장
        broken = [0] * n
        for i in range(n):
            line = input().rstrip()
            for j in range(m):
                if line[j] == 'x':
                    broken[i] |= bit[j]

        # 길이가 m이며 인접하는 1이 없는 비트(state)와 각 비트의 1의 갯수(cnt)
        cand_bits = []
        for b in range(1<<m):
            check = True
            for i in range(m-1):
                if (b & bit[i]) and (b & bit[i+1]):
                    check = False
                    break
            if check:
                state = b
                cnt = 0
                while b:
                    cnt += b % 2
                    b //= 2
                cand_bits.append((state, cnt))

        # 각 행의 dfs(r, pre_state) 값을 저장
        dp = [[-1] * (1<<m) for _ in range(n)]

        # 0번째 행에 학생을 앉힐 차례일 때 앞으로 앉힐 수 있는 최대 학생수
        answer.append(dfs(0, 0))

    return '\n'.join(map(str, answer))


# 이전 행의 상태가 pre이고 현재 행의 상태가 cur 일 때
# 컨닝이 가능한 상태인지 여부를 반환
def is_cheating_possible(pre, cur, m):
    check = False
    for i in range(m):
        if pre & bit[i]:
            if i > 0 and cur & bit[i-1]:
                check = True
                break
            if i < m-1 and cur & bit[i+1]:
                check = True
                break
    return check
