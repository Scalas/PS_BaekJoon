import sys

input = sys.stdin.readline
INF = 10 ** 9


# 15658 연산자 끼워넣기 (2)
# n개의 수 사이에 주어진 연산자를 적절히 끼워넣어 구할 수 있는 최솟값과 최댓값을 구하는문제
def sol15658():
    n = int(input())
    nums = list(map(int, input().split()))
    ops = list(map(int, input().split()))

    def dfs(cur, nxti):
        nonlocal min_val, max_val

        if nxti == n:
            min_val, max_val = min(min_val, cur), max(max_val, cur)
            return

        for op in range(4):
            if ops[op]:
                ops[op] -= 1
                if op == 0:
                    dfs(cur + nums[nxti], nxti + 1)
                elif op == 1:
                    dfs(cur - nums[nxti], nxti + 1)
                elif op == 2:
                    dfs(cur * nums[nxti], nxti + 1)
                elif op == 3:
                    dfs(div(cur, nums[nxti]), nxti + 1)
                ops[op] += 1

    min_val, max_val = INF, -INF
    dfs(nums[0], 1)
    return '\n'.join(map(str, (max_val, min_val)))


def div(a, b):
    if a < 0:
        return -(-a // b)
    return a // b
