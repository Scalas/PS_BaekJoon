import sys

input = sys.stdin.read


# 5557 1학년
# n 개의 숫자가 주어졌을 때, 마지막 두 숫자 사이에 = 을, 나머지 숫자 사이에 + 또는 - 를 넣어
# 성립하는 등식을 만드는 경우의 수를 구하는 문제. 단, 왼쪽에서부터 계산했을 때 중간 과정은 0이상 20 이하여야 한다
def sol5557():
    n, *nums = map(int, input().split())

    # 현 단계에서 만들어질 수 있는 숫자들과 그 경우의 수
    # 초기 상태에서는 첫 번째 숫자 1개만이 존재한다.
    d = {nums[0]: 1}

    for num in nums[1:-1]:
        # 이번 단계에서 만들어질 숫자들
        u = {}

        # 이전 단계에서 만들어진 숫자들에 대해
        for val, cnt in d.items():
            # num 을 더하거나 빼는 것으로 만들어지는 숫자를 구하여
            a, s = val+num, val-num

            # 각 숫자가 0 이상 20 이하라면 이번 단계에서 만들어진 숫자로 추가한다
            if 0 <= a <= 20:
                u[a] = u.get(a, 0) + cnt
            if 0 <= s <= 20:
                u[s] = u.get(s, 0) + cnt

        # 이번 단계에서 만들어진 숫자들로 d 를 대체한다
        d = u

    # 마지막 단계에서 만들어진 숫자들 중 등식의 결과값인 nums[-1] 의 갯수를 구한다
    return d[nums[-1]]
