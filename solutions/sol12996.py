import sys

input = sys.stdin.readline
mod = 1000000007


# 12996 Acka
# 앨범에 포함될 곡의 수와 세 사람이 불러야할 곡의 수가 각각 주어지고
# 앨범에 참여한 사람이 다른 곡이 하나라도 있는 경우 다른 앨범으로 간주한다고 할 때
# 만들 수 있는 앨범의 경우의 수를 구하는 문제
def sol12996():
    n, u, v, w = map(int, input().split())
    
    # 부를 수 있는 곡의 수보다 전체 곡의 수가 더 많을 경우 앨범을 만들 수 없ㅇ므
    if n > (u + v + w):
        return 0

    # 조합 구하기
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = dp[i][i] = 1
        dp[i][1] = i
    for i in range(1, n + 1):
        for j in range(2, i):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod

    answer = 0

    # 한번이라도 불러진 곡 수, 아무도 부르지 않은 곡 수
    a, b = 0, n

    # 첫 사람이 불러야할 곡 선택
    l1 = dp[n][u]
    a, b = u, n - u

    # 두 번째 사람이 불러야할 곡 선택
    # 아직 부르지 않은 곡에서 몇개 선택할지 선택
    for k in range(min(b, v) + 1):
        if b - k > w:
            continue
        l2 = (dp[b][k] * dp[a][v-k]) % mod

        # 세 번째 사람은 아직 부르지않은 곡을 모두 부른 뒤
        # 더 부를 수 있는 곡을 기존에 불렀던 곡에서 선택
        l3 = dp[a + k][w - b + k]

        res = (l1 * l2 * l3) % mod

        answer = (answer + res) % mod

    return answer
