import sys

input = sys.stdin.readline


# 14501 퇴사
# 1일부터 n일 까지의 동시에 진행 불가능한 스케줄과 각 스케줄을 실행했을때의 소요시간, 수익이 주어졋을 때
# n일 동안 낼 수 있는 최대 수익을 구하는 문제
def sol14501():
    # 일수
    n = int(input())

    # profit[k] 는 k일 까지의 최대수익
    profit = [0] * (n + 1)

    for day in range(1, n + 1):
        # 오늘의 스케줄
        t, p = map(int, input().split())

        # 오늘의 스케줄을 실행할 경우 전날까지의 최대수익 + 오늘 스케줄로 얻는 수익을 계산하여
        # 스케줄이 종료되는 날의 수익의 최댓값을 갱신한다.
        if day + t - 1 <= n:
            profit[day + t - 1] = max(profit[day + t - 1], profit[day - 1] + p)

        # 전날 까지의 최대수익으로 오늘까지의 최대수익 값을 갱신
        profit[day] = max(profit[day], profit[day - 1])

    # n일 까지의 최대 수익 반환
    return profit[n]
