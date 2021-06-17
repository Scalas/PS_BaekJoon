import sys

input = sys.stdin.read


# 21965 드높은 남산 위에 우뚝 선
# 주어진 수열이 증가하다가 감소하는 수열인지 판별하는 문제
# 증감이 없는 구간이 있거나 감소구간에 접어들었는데 증가할 경우 NO, 그 외엔 YES
def sol21965():
    n, *nums = map(int, input().split())
    state = True
    for diff in [nums[i + 1] - nums[i] for i in range(n - 1)]:
        if diff == 0:
            return 'NO'
        if state and (diff < 0):
            state = not state
        if not state and diff > 0:
            return 'NO'
    return 'YES'

