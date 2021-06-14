import sys
import math

input = sys.stdin.read


# 4948 베르트랑 공준
# n보다 크고 2n보다 작거나 같은 수 중 소수의 갯수를 구하는 문제
def sol4948():
    # 123456 * 2까지의 자연수의 소수 여부를 미리 구해두고 시작
    nm = 123456*2
    nums = [1] * (nm+1)
    nums[1] = 0
    for i in range(2, int(math.sqrt(nm)) + 1):
        if nums[i] == 1:
            nums[i * 2::i] = [0] * (nm // i - 1)

    # 각 테스트 케이스의 범위에 따라 소수의 갯수를 구함
    answer = []
    for m in map(int, input().split()):
        if m == 0:
            break
        n = 2 * m
        cnt = 0
        if m <= 2 and n >= 2:
            cnt += 1
        cnt += sum(nums[m + 1 - m % 2:n+1:2])
        answer.append(str(cnt - nums[m]))
    print('\n'.join(answer))
