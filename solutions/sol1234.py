import sys

input = sys.stdin.readline


# 1234 크리스마스 트리
# 최대 10개의 층으로 이루어진 트리의 각 층에 3 가지 색의 장난감을 채워서
# 트리를 장식하는 경우의 수를 구하는 문제
# 단, 트리의 i층에는 i개의 장난감을 장식해야하며
# 한 층에 있는 서로 다른 색의 장난감들의 갯수는 같아야한다. (ex: 6층 - 빨강 3 / 파랑 3)
def sol1234():

    n, red, green, blue = map(int, input().split())

    # 모든 층을 한가지 색으로 채워도 10층까지 55개를 넘지 않음
    # 55개를 넘는 색은 55개로 간주하여 탐색할 경우의 수를 줄일 수 있음
    if red > 55:
        red = 55
    if green > 55:
        green = 55
    if blue > 55:
        blue = 55

    # 전체 색상의 수
    total = red + green + blue

    # ntotal[i]는 0부터 i까지의 수를 더한 값
    ntotal = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    
    # fact[i] 는 i의 팩토리얼값
    fact = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

    # dp[i][j][k] 는 채워야할 트리의 층수가 i이고 빨강색 장난감이 j개,
    # 초록색 장난감이 k개 남은 상태일 때 남은 장난감으로 트리를 끝까지 장식할 수 있는 경우의 수
    dp = [[[-1] * 56 for _ in range(56)] for _ in range(11)]

    # 층마다 색의 조합을 선택하며 경우의 수 탐색
    def dfs(level, r, g):
        # 모든 층을 장식했을 경우 1 반환
        if level > n:
            return 1

        if dp[level][r][g] < 0:
            # 남은 장난감의 총 갯수
            t = total - ntotal[level - 1]

            # 파란색의 갯수는 남은 장난감의 총 갯수와 빨강, 초록 장난감의 갯수를 알면 구할 수 있음
            b = t - r - g

            # 남은 장난감으로 트리를 장식하는 경우의 수
            res = 0

            # 2의 배수층인 경우 두 가지 색 선택가능
            if not level % 2:
                # 2가지 색으로 채울 경우 필요한 갯수
                required = level // 2

                # 빨강, 초록
                if r >= required and g >= required:
                    res += dfs(level + 1, r - required, g - required) * (fact[level] // (fact[required] ** 2))

                # 빨강, 파랑
                if r >= required and b >= required:
                    res += dfs(level + 1, r - required, g) * (fact[level] // (fact[required] ** 2))

                # 파랑, 초록
                if b >= required and g >= required:
                    res += dfs(level + 1, r, g - required) * (fact[level] // (fact[required] ** 2))

            # 3의 배수층인 경우 세 가지 색 선택 가능
            if not level % 3:
                # 3가지 색으로 채울 경우 필요한 갯수
                required = level // 3
                if r >= required and g >= required and b >= required:
                    res += dfs(level + 1, r - required, g - required) * (fact[level] // (fact[required] ** 3))

            # 1가지 색으로 모두 채우는 경우
            if r >= level:
                res += dfs(level + 1, r - level, g)
            if g >= level:
                res += dfs(level + 1, r, g - level)
            if b >= level:
                res += dfs(level + 1, r, g)

            # 모든 경우의 수를 더한 값을 저장
            dp[level][r][g] = res

        # 저장된 값을 반환
        return dp[level][r][g]

    # 첫 번째 층을 장식할 차례이고 아무 색도 쓰지 않은 상태에서 트리를 장식할 수 있는 모든 경우의 수
    return dfs(1, red, green)
