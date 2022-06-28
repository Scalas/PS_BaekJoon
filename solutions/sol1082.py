import sys

input = sys.stdin.readline


# 1082 방 번호
# 0부터 최대 n - 1까지의 번호를 각각 정해진 가격으로 여러번 구매 가능할 때
# m의 돈으로 번호를 사서 이어붙여 만들 수 있는 가장 큰 번호를 구하는 문제
def sol1082():
    n = int(input())
    p = list(map(int, input().split()))
    nums = []
    for i in range(n):
        nums.append([p[i], i])
    nums.sort()
    m = int(input())

    if n == 1:
        return 0

    # 만들 수 있는 최대 자릿수를 구함
    selected = []

    # 가장 싼 번호와 가격
    min_cost, min_num = nums[0]

    # 만약 가장 싼 번호가 0이 아니라면 최대한 많이 구매
    if min_num:
        selected += [min_num] * (m // min_cost)
        m %= min_cost
    # 가장 싼 번호가 0이라면 하나는 두 번째로 싼 번호를 구매
    else:
        selected.append(nums[1][1])
        m -= nums[1][0]
        # 만약 두 번째로 싼 번호를 살 수 없다면 만들 수 있는 번호는 0뿐
        if m < 0:
            return 0
        selected += [min_num] * (m // min_cost)
        m %= min_cost

    # 맨 앞자리부터 최대한 큰 수로 바꿔나감
    for i in range(len(selected)):
        num = selected[i]
        # 기존 가격
        org = p[num]

        # 가장 큰 수부터 바꿀 수 있는지 탐색
        for chg_num in range(n-1, num, -1):
            chg = p[chg_num]
            if chg - org <= m:
                selected[i] = chg_num
                m -= (chg - org)
                break

    return ''.join(map(str, sorted(selected)[::-1]))
