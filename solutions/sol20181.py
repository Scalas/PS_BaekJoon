import sys

input = sys.stdin.readline


def sol20181():
    n, k = map(int, input().split())
    food = list(map(int, input().split()))
    food.append(0)
    for i in range(n-1):
        food[i+1] += food[i]

    # satisfaction[i]는 i부터 먹이를 먹기 시작할 때
    # 얻을 수 있는 탈피에너지와 연속으로 먹이를 먹는것이 끝나는 칸
    satisfaction = []
    s, e = 0, 0
    while e < n:
        # s부터 e까지 얻은 만족도의 합
        sat = food[e] - food[s-1]

        # 만족도가 k 이상일 경우
        # s에서 먹이를 먹기 시작할 경우 축적 가능한 탈피에너지와
        # 먹이를 먹는 것이 끝나는 지점을 dp에 저장
        # s를 한칸 앞으로
        if sat >= k:
            satisfaction.append((sat - k, e))
            s += 1
        else:
            e += 1

    while s < n:
        satisfaction.append((food[n-1] - food[s-1] - k, n-1))
        s += 1

    # 현재 칸 i에서 앞으로 얻을 수 있는 최대 탈피에너지는
    # 현재 칸의 먹이를 포기하고 다음 칸부터 얻을 수 있는 최대 탈피에너지와
    # 현재 칸의 먹이를 먹고 얻은 탈피에너지와 먹기가 끝나는 시점부터 얻을 수 있는 탈피에너지의 합중 최댓값
    dp = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        dp[i] = max(satisfaction[i][0] + dp[satisfaction[i][1]+1], dp[i+1])

    # 시작지점에서 출발하여 얻을 수 있는 최대 탈피에너지 반환
    return dp[0]
