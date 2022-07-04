import sys

input = sys.stdin.readline


# 1016 제곱 ㄴㄴ 수
# min이상 max이하의 정수중에서 1보다 큰 제곱수로 나누어 떨어지지 않는 수의 갯수를 구하는 문제
def sol1016():
    min_val, max_val = map(int, input().split())
    nums = [1] * (max_val - min_val + 1)
    n = len(nums)
    # i = 2부터 시작해서 i의 제곱이 max를 넘지 않을 때 까지 반복
    i = 2
    sqrt = int(max_val**.5)
    while i < sqrt + 1:
        # 제곱으로 나누어떨어지는 가장 작은 수부터 제곱수만큼 더해가며 지워나감
        sq = i * i
        remain = min_val % sq
        if not remain:
            nums[0] = 0
        s = sq - min_val % sq
        for j in range(s, n, sq):
            nums[j] = 0
        i += 1
    
    # 제곱수의 배수로 지워지지 않은 수의 갯수를 반환
    return sum(nums)
