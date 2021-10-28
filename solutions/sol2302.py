import sys

input = sys.stdin.read


# 2302 극장 좌석
# 1~n번 까지의 일렬로된 좌석에서 m개의 고정좌석이 주어지고
# 원래 자리에서 1칸 떨어진 자리까진 자리이동이 가능하다고 할 때
# 가능한 모든 좌석배치 경우의 수를 구하는 문제
def sol2302():
    n, m, *fixed = map(int, input().split())
    fixed.append(n+1)
    fixed.append(0)
    # 좌석이 k개고 원래자리에서 1칸 떨어진 자리까지 자리이동이 가능할때 가능한 모든 경우의 수를 dp[k] 라 할 때
    # 고정된 좌석을 기준으로 사이사이에 있는 좌석의 갯수에 대해 dp값을 모두 구하여 곱해주면 된다.
    query = [fixed[i]-fixed[i-1]-1 for i in range(m+1)]

    # 좌석이 0개일 경우 1, 1개일 경우 1, 2개일 경우 2로 초기화
    dp = [1, 1, 2]

    # 좌석이 3개 이상일 경우 dp[k] = dp[k-1] + dp[k-2]
    for _ in range(2, max(query)):
        dp.append(dp[-1] + dp[-2])

    # 고정좌석 사이의 모든 좌석들에 대해 dp값을 구하여 곱한다.
    answer = 1
    for q in query:
        answer *= dp[q]
    return answer
