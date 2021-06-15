import sys

input = sys.stdin.read


# 9020 골드바흐의 추측
# 짝수 n이 주어졌을때 합이 n 이되는 차가 가장 적은 두 소수를 구하는 문제
# n의 최대치까지의 소수를 미리 구해두고 n//2부터 가장 가까운 소수를 탐색
def sol9020():
    nums = [1] * 10001
    nums[1] = 0
    for i in range(2, 100):
        if nums[i] != 0:
            nums[i * 2::i] = [0] * (10000 // i - 1)

    _, *cases = map(int, input().split())
    answer = []
    for c in cases:
        s = c // 2
        while (nums[s] == 0 or nums[c - s] == 0):
            s -= 1
        answer.append(f'{s} {c - s}')
    print('\n'.join(answer))
