import sys

input = sys.stdin.readline


# 2295 세 수의 합
# n개의 수에서 중복에 상관없이 3 번 수를 골라 더했을 때 나온 수 또한 n개의 수 중에 있을 경우
# 세 수의 합으로 가능한 가장 큰 수를 구하는 문제
def sol2295():
    n = int(input())
    single_nums = [int(input()) for _ in range(n)]
    single_nums.sort()

    # 두 수를 더해서 만들 수 있는 수를 모두 탐색
    double_nums = set()
    for i in range(n):
        for j in range(n):
            double_nums.add(single_nums[i] + single_nums[j])

    # 가장 큰 수 (i번째 수), 나머지 하나의 수 두개를 골라
    # 두 수의 차가 두 수를 더해서 만들 수 있는 수에 존재하는지 확인
    # 존재한다면 i를 가장 큰 수부터 탐색했을 때 가장 먼저 찾은 조건을 만족하는 i번째 수가 답이 된다.
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            if single_nums[i] - single_nums[j] in double_nums:
                return single_nums[i]
